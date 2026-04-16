# MooTube
o MooTube é um gerenciador de downloads do youtube com capacidade de organização básica e pesquisa.

## AVISO!!!
esse projeto ainda está muito básico, não é pra produção.

## funcionalidades

- gerenciar videos
    - videos do youtube
    - videos próprios
- baixar vídeos externos
    - via ytsearch do yt-dlp
    - baixa um video apenas

## como instalar

para instalar temos dois métodos oficiais, Dockerfile e manual

## método Dockerfile(recomendado para uso no pc principal)

primeiro clone o dockerfile

```bash
wget https://raw.githubusercontent.com/pixelcatBR/mootube/main/Dockerfile
```
após isso gere uma build dele

```bash
sudo docker build -t mootube
```
e após tudo isso execute
```bash
sudo docker run -it mootube
```
## método manual (recomendado pra servers selfhost)

para instalar primeiro precisamos copiar o código fonte do github em zip, via gitclone ou interface gráfica

após isso abra o zip já extraído e crie um venv
``` bash
python -m venv mootube
```
após isso entre no venv
``` bash
source mootube/bin/activate
```
depois instale as dependências no venv
``` bash
pip install flask yt-dlp
```
agora crie a pasta videos
``` bash
mkdir videos
```
e após tudo isso execute.
``` bash
python3 main.py
```

## licença
 esse projeto está licensiado sobre a licença do mit, leia o arquivo de licença para mais detalhes

## contribuição
contribua fazendo forks e pullrequests.

