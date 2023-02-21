FROM python:3.11-alpine

WORKDIR /home
COPY ./core /home/core
COPY ./static /home/static
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

