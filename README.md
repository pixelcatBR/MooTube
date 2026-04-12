# MooTube
o MooTube é um gerenciador de downloads do youtube com capacidade de organização básica e pesquisa.
## funcionalidades

- gerenciar videos
    - videos do youtube
    - videos próprios
- baixar vídeos externos
    - via ytsearch do yt-dlp
    - baixa um video apenas

## como instalar

para instalar primeiro precisamos copiar o código fonte do github em zip
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
e após tudo isso execute.
``` bash
python3 main.py
```

## licença
 esse projeto está licensiado sobre a licença do mit, leia o arquivo de licença para mais detalhes

## contribuição
contribua fazendo forks e pullrequests, não tem muitas regras
## aviso
esse projeto ainda está muito básico, não é pra produção.

