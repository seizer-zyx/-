FROM ubuntu:20.04

RUN sed -i 's/archive.ubuntu.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN pip3 install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN mkdir /app

WORKDIR /app

COPY app /app
COPY flag /

ENTRYPOINT python3 /app/app.py

EXPOSE 80
