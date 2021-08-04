FROM python:3.9.0

RUN groupadd -r syllabus-getter && useradd -r -g syllabus-getter syllabus-getter
RUN apt-get update && apt install -y postgresql-client

COPY ./syllabus-get-server /app
COPY ./models /app/models

WORKDIR /app

RUN pip install -r requirements.txt

USER syllabus-getter

CMD ["/app/cmd.sh"]