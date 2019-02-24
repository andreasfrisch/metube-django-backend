FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc python-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev mariadb-dev
RUN apk add build-base

WORKDIR /metube/src
EXPOSE 8000

# RUN pip install -U setuptools wheel
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /metube

ENTRYPOINT ["./docker_entrypoint.sh"]