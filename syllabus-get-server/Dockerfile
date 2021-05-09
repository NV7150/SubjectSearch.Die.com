FROM tiangolo/uvicorn-gunicorn:python3.8

LABEL maintainer="Sebastian Ramirez <tiangolo@gmail.com>"

RUN groupadd -r syllabus-getter && useradd -r -g syllabus-getter syllabus-getter
RUN pip install --no-cache-dir fastapi

COPY . /app

USER syllabus-getter