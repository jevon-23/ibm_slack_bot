# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ARG SLACK_BOT_TOKEN
ARG SLACK_APP_TOKEN

RUN echo $SLACK_BOT_TOKEN
RUN echo $SLACK_APP_TOKEN
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
