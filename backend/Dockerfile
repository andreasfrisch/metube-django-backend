FROM python:3.5-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc python-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev mariadb-dev \
    && pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app/metube

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn","-b","0.0.0.0:8000","metube.wsgi:application"]