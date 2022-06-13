FROM python:3.9.5-alpine

WORKDIR /home/JustPub

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .