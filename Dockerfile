# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ARG BOT_TOK
ARG APP_TOK

ENV SLACK_BOT_TOKEN=${BOT_TOK}
ENV SLACK_APP_TOKEN=${APP_TOK}

RUN echo $SLACK_BOT_TOKEN
RUN echo $SLACK_APP_TOKEN
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
