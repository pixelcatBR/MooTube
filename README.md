# MooTube
o MooTube é um gerenciador de downloads do youtube selfhost com capacidade de organização básica e pesquisa.

## AVISO!!!
esse projeto ainda está muito básico, não é pra produção ou exposição. mas ele pode ser usado em rede local

## funcionalidades

- gerenciar videos
    - videos do youtube
- baixar vídeos externos
    - via ytsearch do yt-dlp
    - baixa um video apenas

## como instalar

para instalar temos dois métodos oficiais, Dockerfile e manual

## método Dockerfile(recomendado por ser fácil de instalar)

dê docker run

```bash
sudo docker run -it -p 5000:5000 pixelcatbr/mootube
```
acesse a interface web pelo endereço no terminal e pronto
## método manual (recomendado pra uso avançado e estudo do código)

para instalar primeiro precisamos copiar o código fonte do github em zip, via git clone ou interface gráfica

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
ele vai te dar o ip e é só usar

## licença
 esse projeto está licensiado sobre a licença do mit, leia o arquivo de licença para mais detalhes

## contribuição
contribua fazendo forks e pullrequests.

