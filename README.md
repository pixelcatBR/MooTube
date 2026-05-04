# MooTube
o MooTube é um gerenciador de downloads do youtube selfhost com capacidade de organização básica e pesquisa.

## Aviso
esse projeto está até funcional, mas não recomendo expor na internet se você tiver conhecimento técnico 

## funcionalidades

- gerenciar videos
    - videos do youtube
- baixar vídeos externos
    - via ytsearch do yt-dlp
    - baixa um video apenas

## como instalar

para instalar temos dois métodos oficiais, Dockerfile e manual

## método Dockerfile(recomendado por ser fácil de instalar)

primeiro abra o seu programa de tetminal e digite isso:

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

## licença
 esse projeto está licensiado sobre a licença do mit, leia o arquivo de licença para mais detalhes

## contribuição
contribua fazendo forks e pullrequests.

