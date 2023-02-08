FROM python:latest

WORKDIR /home
COPY ./core /home/core
COPY requirements.txt .

RUN pip install -r requirements.txt
# RUN psql postgresql+asyncpg://ndushakov:1234567890@db:5432/okkam 