# MooTube
o MooTube é um gerenciador de downloads do youtube selfhost com capacidade de organização básica e pesquisa.

## Aviso
esse projeto está até funcional, mas não recomendo expor na internet se você tiver conhecimento técnico para isso

## funcionalidades

- gerenciar videos
    - contamos com um sistema de gerenciamento de vídeos 
- baixar vídeos externos
    - integração com downloads de vídeos do YouTube

## como instalar

para instalar temos dois métodos oficiais, Dockerfile e manual

## método Dockerfile(recomendado por ser fácil de instalar e com melhor suporte)

primeiro abra o seu programa de terminal e digite isso:

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
- verifique se não há uma nova atualização, aperte o botão atualizar e verificar que você vai baixar a versão mais recente.
- após atualizar use sudo docker stop mootube-server e depois use sudo docker start -i mootube-server para reiniciar
- use sudo docker start -i mootube-server após ter rodado o run uma vez para rodar mootube com os vídeos que você já baixou.
## licença
 esse projeto está licenciado sobre a licença do mit, leia o arquivo de licença para mais detalhes

## contribuição
contribua fazendo forks e pullrequests.

