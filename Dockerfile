FROM python:3.10-slim-buster

ARG APP_PORT
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . /app
EXPOSE $APP_PORT
