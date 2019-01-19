FROM python:3.6-alpine
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    ca-certificates gcc python-dev linux-headers musl-dev \
    libffi-dev jpeg-dev zlib-dev mariadb-dev
RUN apk add build-base

# RUN pip install -U setuptools wheel
RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app/metube

EXPOSE 8000

ENTRYPOINT ["./docker_entrypoint.sh"]