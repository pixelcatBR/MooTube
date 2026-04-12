from flask import Flask, render_template, send_from_directory, request, abort
import os
import subprocess
import re

app = Flask(__name__)

# Pasta onde ficam os vídeos
PASTA_VIDEOS = "videos"

# Cria a pasta se não existir
os.makedirs(PASTA_VIDEOS, exist_ok=True)

@app.route('/')
def index():
    """Página inicial - lista os vídeos"""
    
    # Lê todos os vídeos da pasta
    videos = []
    for arquivo in os.listdir(PASTA_VIDEOS):
        if arquivo.endswith(('.mp4', '.webm', '.mkv')):
            videos.append(arquivo)
    
    return render_template('index.html', videos=videos)

@app.route('/video/<nome_video>')
def serve_video(nome_video):
    """Serve o arquivo de vídeo"""
    
    return send_from_directory(PASTA_VIDEOS, nome_video)

@app.route('/pesquisar')
def pesquisar():
    """Pesquisa e baixa o primeiro vídeo do YouTube"""
    
    termo = request.args.get("busca")
    
    if not termo:
        return "Nenhum termo de busca fornecido.", 400
    
    print(f"📥 Baixando: {termo}")
    
    # Limpa o nome do arquivo para evitar problemas
    nome_limpo = re.sub(r'[^\w\s-]', '', termo)
    
    # Comando para baixar o primeiro resultado da busca
    cmd = [
        "yt-dlp",
        f"ytsearch1:{termo}",
        "-o", f"{PASTA_VIDEOS}/%(title)s.%(ext)s",
        "--no-warnings",
        "--restrict-filenames"
    ]
    
    try:
        # Executa o download
        resultado = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(f"✅ Download concluído: {termo}")
        
        # Retorna página de sucesso com redirect automático
        return """
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="2; url=/">
            <title>Download concluído - MooTube</title>
            <style>
                body {
                    background-repeat: repeat;
                    background-size: 100px;
                    margin: 0;
                    background-color: rgb(240, 238, 238);
                    font-family: Arial, Helvetica, sans-serif;
                    min-height: 100vh;
                }
                .container {
                    text-align: center;
                    padding-top: 200px;
                }
                h1 {
                    color: #333;
                    font-size: 28px;
                }
                p {
                    color: #666;
                    font-size: 18px;
                }
                .emoji {
                    font-size: 64px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="emoji">🐮✅</div>
                <h1>Download concluído!</h1>
                <p>O vídeo foi adicionado à sua biblioteca.</p>
                <p>Redirecionando em 2 segundos...</p>
            </div>
        </body>
        </html>
        """
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro no download: {e.stderr}")
        
        # Retorna página de erro
        return f"""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="refresh" content="3; url=/">
            <title>Erro - MooTube</title>
            <style>
                body {{
                    background-repeat: repeat;
                    background-size: 100px;
                    margin: 0;
                    background-color: rgb(240, 238, 238);
                    font-family: Arial, Helvetica, sans-serif;
                    min-height: 100vh;
                }}
                .container {{
                    text-align: center;
                    padding-top: 200px;
                }}
                h1 {{
                    color: #d32f2f;
                    font-size: 28px;
                }}
                p {{
                    color: #666;
                    font-size: 18px;
                }}
                .emoji {{
                    font-size: 64px;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="emoji">🐮❌</div>
                <h1>Erro ao baixar vídeo</h1>
                <p>Não foi possível encontrar ou baixar o vídeo.</p>
                <p>Redirecionando em 3 segundos...</p>
            </div>
        </body>
        </html>
        """, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
