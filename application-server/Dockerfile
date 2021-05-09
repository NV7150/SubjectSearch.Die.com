FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN groupadd -r syllabus-getter && useradd -r -g syllabus-getter syllabus-getter

COPY . /app
RUN pip install -U pip \
     && pip install -r /app/requirements.txt

USER syllabus-getter
