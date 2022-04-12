# syntax=docker/dockerfile:1

FROM ubuntu

WORKDIR /projects/

COPY requirements.txt requirements.txt

COPY instantclient_21_5 instantclient_21_5

RUN apt update

RUN apt install -y libaio1

RUN apt install -y python3

RUN apt install -y python3-pip

RUN pip3 install --upgrade pip

RUN apt install -y mysql-client

RUN apt install -y libmysqlclient-dev

RUN apt install -y git

RUN pip3 install -r requirements.txt

ENV LD_LIBRARY_PATH /projects/instantclient_21_5:$LD_LIBRARY_PATH

ENV TZ=Asia/Shanghai

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone