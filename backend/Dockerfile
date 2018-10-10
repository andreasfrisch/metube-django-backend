#consider python:3.5-alpine
FROM python:3.5

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app
WORKDIR /app/metube

EXPOSE 8000

ENTRYPOINT ["/usr/local/bin/gunicorn","-b","0.0.0.0:8000","metube.wsgi:application"]