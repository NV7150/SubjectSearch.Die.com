FROM python:3.9.0

RUN groupadd -r syllabus-getter && useradd -r -g syllabus-getter syllabus-getter

COPY . /app

WORKDIR /app

USER syllabus-getter
CMD ["/app/cmd.sh"]