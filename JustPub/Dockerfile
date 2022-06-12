FROM python:3.9.5-alpine

# set work directory
WORKDIR /home/JustPub

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# copy project
COPY . .
