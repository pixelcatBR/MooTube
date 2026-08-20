# MooTube
o MooTube é um reprodutor de vídeos web auto-hospedado integrado com yt-dlp.

## Aviso!
```não exponha o mootube à internet, ele é uma aplicação projetada pra usar em rede lan e pode ser perigoso.```
## funcionalidades

- listar vídeos com fotos automáticas do embed
- reproduzir vídeos baixados no embed do navegador
- baixar vídeos via yt-dlp
- baixar vídeos do urls.txt
## Como atualizar
1. Acesse a interface web
2. Clique no botão 🔄 no canto superior
3. Pronto! O MooTube se atualiza sozinho
## como instalar

para instalar temos dois métodos oficiais, Docker e manual

## método Docker(recomendado por ser fácil de instalar e com melhor suporte)
primeiro abra o terminal do seu servidor e digite isso:
```bash
sudo docker run --name mootube-server -p 5000:5000 pixelcatbr/mootube
```
acesse a interface web pelo endereço na tela e pronto
## método manual (recomendado pra uso avançado e estudo do código)

para instalar primeiro precisamos copiar o código fonte do github em zip, via git clone ou interface gráfica

após isso abra o zip já extraído e crie um venv
``` bash
python -m venv venv
```
após isso entre no venv
``` bash
source venv/bin/activate
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
ele vai te dar o ip e é só usar
## passos pós instalação
após instalar:
- baixe alguns vídeos e salve para você assistir sem internet.
- crie seu urls.txt para beckup dos seus vídeos
- verifique se não há uma nova atualização, aperte o botão atualizar que ele vai baixar a versão mais recente automaticamente.
- use ```sudo docker start -i mootube-server``` após ter finalizado o run para rodar mootube com as suas configurações e atualizações.
## licença
 esse projeto está licenciado sobre a licença do mit, tome cuidado ao distribuir o código.

## contribuição
contribua com o projeto mootube, fazendo dês de uma tradução simples até uma segurança completa, aceito qualquer ajuda.

