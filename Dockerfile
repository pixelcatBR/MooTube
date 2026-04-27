FROM ubuntu:latest

RUN apt-get update && apt-get install -y python3 pip
RUN pip install --break-system-packages flask yt-dlp

RUN git clone https://github.com/pixelcatBR/mootube.git

WORKDIR /mootube
RUN mkdir -p videos

CMD ["python3", "main.py"]
