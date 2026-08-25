# MooTube
o MooTube é um reprodutor de vídeos web auto-hospedado integrado com yt-dlp.

## Aviso!
```não exponha o mootube à internet, ele é uma aplicação projetada pra usar em rede lan e pode ser perigoso.```
## funcionalidades
- integração com o downloader yt-dlp
- compartilhamento/automação de downloads por arquivo urls.txt
- streaming do server em lan via inrterface web
- interface web disponível na porta 5000
- Atualização simples e prática


## Feature de atualizar
temos um sistema de atualização focado em praticidade e simplicidade.
### Como usar
1. Acesse a interface web
2. Clique no botão 🔄 no canto superior
3. Pronto! O MooTube se atualiza sozinho
## como instalar

para instalar temos dois métodos oficiais, Docker e manual

### método Docker(recomendado por ser fácil de instalar e com melhor suporte)
primeiro abra o terminal do seu servidor e digite isso:
```bash
sudo docker run --name mootube-server -p 5000:5000 pixelcatbr/mootube
```
acesse a interface web pelo endereço na tela e pronto
### método manual (não recomendado para uso diário)

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
pip install -r requirements.txt
```
agora crie a pasta videos
``` bash
mkdir videos
```
e após tudo isso execute.
``` bash
python3 main.py
```
ele vai te dar o endereço e é só usar

## diferença entre método de instalação docker e manual

Caso esteja indeciso sobre qual escolher, aqui vão as vantagens e desvantagens de cada um
### Docker
ele é o método mais recomendado atualmente por ser simples de usar, com melhor suporte e com menos chances de quebrar o sistema hospedeiro, se quebrar, quebra só ele, ideal para uso diário. ele incluí:
- melhor suporte para updates
- maior simplicidade
- não quebra o sistema hospedeiro

### Manual

Este é o método mais complexo, ele exige mais conhecimento e técnicas pra não quebrar o sistema, como o venv por exemplo, ideal para desenvolvedores que querem contribuir. ele incluí
- instalação mais complexa
- edição facíl do código
- melhor para manutenções manuais
- mais trabalhoso
## passos pós instalação
após instalar:
- Atualize o MooTube para a versão mais recente, isso garante que ele terá todas features.
- Olhe as features novas pelo menu de features.
- baixe alguns vídeos e salve para você assistir sem depender de serviços externos.
- crie seu urls.txt para compartilhar seus videos com amigos ou baixar coleções da internet.
- após dias de uso, verifique se não há novos updates, especialmente em versões em desenvolvimento.
- use ```sudo docker start -i mootube-server``` após ter finalizado o run para rodar seu mootube novamente.
## licença
 esse projeto está licenciado sobre a licença do mit, tome cuidado ao distribuir o código.

## contribuição
contribua com o projeto mootube, fazendo dês de uma tradução simples até uma segurança completa, aceito qualquer ajuda.

