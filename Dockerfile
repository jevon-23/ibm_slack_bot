# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

ARG SLACK_BOT_TOKEN=${SLACK_BOT_TOKEN:-default}
ARG SLACK_APP_TOKEN=${SLACK_APP_TOKEN:-default}
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "app.py"]
