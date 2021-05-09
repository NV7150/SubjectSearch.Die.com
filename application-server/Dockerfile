FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN groupadd -r app && useradd -r -g app app

COPY . /app
RUN pip install -U pip \
     && pip install -r /app/requirements.txt

USER app
