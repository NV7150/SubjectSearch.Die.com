FROM python:3.9.0

RUN groupadd -r syllabus-getter && useradd -r -g syllabus-getter syllabus-getter
RUN apt-get update && apt install -y postgresql-client

COPY ./syllabus_get_server /app/syllabus_get_server
COPY ./models /app/models
COPY ./test_cases /app/test

WORKDIR /app

RUN pip install -r syllabus_get_server/requirements.txt

USER syllabus-getter

# if you want to run unit test, you should set TEST to 1
ENV TEST 0

CMD ["/app/syllabus_get_server/cmd.sh"]