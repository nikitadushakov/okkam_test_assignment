FROM python:latest

WORKDIR /home
COPY ./core /home/core
COPY ./static /home/static
COPY requirements.txt .

RUN pip install -r requirements.txt