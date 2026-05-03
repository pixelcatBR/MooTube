from flask import Flask, render_template, send_from_directory, request, abort
import os
import subprocess
import re
import time
from pathlib import Path
from functools import wraps
from datetime import datetime

app = Flask(__name__)

PASTA_VIDEOS = "videos"
MAX_FILE_SIZE = 2 * 1024 * 1024 * 1024 
ALLOWED_EXTENSIONS = {'.mp4', '.webm', '.mkv', '.avi', '.mov'}
MAX_SEARCH_LENGTH = 200
DOWNLOAD_TIMEOUT = 300 
RATE_LIMIT = 15 


rate_limit_store = {}

def rate_limit(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        client_ip = request.remote_addr
        now = time.time()
        
        if client_ip not in rate_limit_store:
            rate_limit_store[client_ip] = []
        
        rate_limit_store[client_ip] = [
            req_time for req_time in rate_limit_store[client_ip]
            if now - req_time < 60
        ]
        
        if len(rate_limit_store[client_ip]) >= RATE_LIMIT:
            return "Limite de downloads excedido. Aguarde um momento.", 429
        
        rate_limit_store[client_ip].append(now)
        return f(*args, **kwargs)
    return decorated_function

def sanitize_filename(filename):
    """Sanitiza o nome do arquivo de forma segura"""

    filename = re.sub(r'[^\w\s\-\.]', '', filename)

    filename = re.sub(r'\s+', ' ', filename)

    filename = filename[:200]
    return filename.strip()

def validate_video_path(filename):
    """Valida se o caminho do vídeo é seguro"""

    safe_path = os.path.normpath(os.path.join(PASTA_VIDEOS, filename))
    if not safe_path.startswith(os.path.normpath(PASTA_VIDEOS)):
        return False, None

    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        return False, None
    
    return True, safe_path

os.makedirs(PASTA_VIDEOS, exist_ok=True)

@app.route('/')
def index():
    """Página inicial - lista os vídeos"""
    

    videos = []
    for arquivo in os.listdir(PASTA_VIDEOS):
        if arquivo.endswith(tuple(ALLOWED_EXTENSIONS)):

            is_safe, _ = validate_video_path(arquivo)
            if is_safe:
                videos.append(arquivo)
    
    return render_template('index.html', videos=videos)

@app.route('/video/<path:nome_video>')
def serve_video(nome_video):
    """Serve o arquivo de vídeo com segurança"""

    nome_video_safe = sanitize_filename(nome_video)
    
    is_safe, _ = validate_video_path(nome_video_safe)
    if not is_safe:
        abort(404)
    
    response = send_from_directory(PASTA_VIDEOS, nome_video_safe)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    return response

@app.route('/pesquisar')
@rate_limit
def pesquisar():
    """Pesquisa e baixa o primeiro vídeo do YouTube"""
    
    termo = request.args.get("busca", "").strip()
    
    if not termo:
        return "Nenhum termo de busca fornecido.", 400

    if len(termo) > MAX_SEARCH_LENGTH:
        return "Termo de busca muito longo.", 400

    termo_seguro = re.sub(r'[;&|`$<>]', '', termo)
    
    print(f"📥 Baixando: {termo_seguro}")
    
    videos_path = Path(PASTA_VIDEOS).resolve()
    
    cmd = [
        "yt-dlp",
        f"ytsearch1:{termo_seguro}",
        "-o", str(videos_path / "%(title)s.%(ext)s"),
        "--no-warnings",
        "--restrict-filenames",
        "--no-playlist", 
        "--socket-timeout", "30"
    ]
    
    try:

        resultado = subprocess.run(
            cmd, 
            check=True, 
            capture_output=True, 
            text=True,
            timeout=DOWNLOAD_TIMEOUT
        )
        
        print(f"✅ Download concluído: {termo_seguro}")
        return render_template('sucess.html')

        
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout no download")
        return render_template('timeout.html')
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no download: {e.stderr}")

        return render_template('error.html')

@app.after_request
def add_security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    return response

@app.route("/atualizar")
def atualizar():
    try:
        subprocess.run(["pip", "install", "-U", "flask", "yt-dlp", "--break-system-packages"], check=True, capture_output=True)
        subprocess.run("git clone https://github.com/mootube-project/mootube && cp -r mootube/* . && rm -rf mootube", 
                      shell=True, check=True, capture_output=True)
        return render_template('update-sucess.html')
    except subprocess.CalledProcessError as e:
        print(f"Erro: {e.stderr}")
        return render_template('update-error.html')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=5000)
