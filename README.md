# MooTube
o MooTube é um reprodutor de vídeos web auto-hospedado integrado com yt-dlp.

## Aviso!
```não exponha o mootube a internet, ele é uma aplicação insegura e pode ser perigoso.```
## funcionalidades

- listar vídeos com fotos automáticas do embed
- reproduzir vídeos baixados no embed do navegador
- baixar vídeos via yt-dlp
- baixar vídeos do urls.txt

## como instalar

para instalar temos dois métodos oficiais, Docker e manual

## método Docker(recomendado por ser fácil de instalar e com melhor suporte)
primeiro abra o terminal do seu servidor e digite isso:

```bash
mkdir ~/mootube && sudo docker run --name mootube-server -p 5000:5000 -v ~/mootube:/mootube/videos pixelcatbr/mootube
```
ou digite isso (caso queira algo mais simples)
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
- importe vídeos no mootube pela pasta mootube e assista eles
- crie seu urls.txt para seus vídeos na internet
- troque a pasta ```~/videos``` do comando ```mkdir ~/videos``` e ```-v ~/videos``` e também troque o nome modificando o texto depois de ```--name``` para poder ter múltiplos mootubes, exemplo: ```mkdir ~/mootube-criancas && sudo docker run --name mootube-criancas -p 5000:5000 -v ~/mootube-criancas:/mootube/videos pixelcatbr/mootube```
- verifique se não há uma nova atualização, aperte o botão atualizar e verificar que você vai baixar a versão mais recente.
- após atualizar use ```sudo docker stop mootube-server && sudo docker start -i mootube-server``` para reiniciar
- use ```sudo docker start -i mootube-server``` após ter rodado o run uma vez para rodar mootube com as suas configurações e atualizações.
## licença
 esse projeto está licenciado sobre a licença do mit, tome cuidado ao distribuir o código.

## contribuição
contribua com o projeto mootube, fazendo dês de uma tradução simples até uma segurança completa, aceito qualquer ajuda.

