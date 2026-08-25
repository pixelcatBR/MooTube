FROM ubuntu:latest

WORKDIR /app/

RUN apt-get update && \
    apt-get install -y python3 python3-pip git

RUN git clone "https://github.com/themooproject/mootube"

WORKDIR /app/mootube

RUN pip install --break-system-packages -r requirements.txt

RUN mkdir videos

CMD ["python3", "main.py"]
