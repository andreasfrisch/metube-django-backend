FROM python:3.5

ENV PYTHONUNBUFFERED 1

# RUN groupadd -r django \
    # && -r -g django django

# Requirements have to be pulled and installed here, otherwise caching won't work
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt 
    # && rm -rf /requirements

# COPY ./compose/django/gunicorn.sh ./compose/django/entrypoint.sh /
# RUN sed -i 's/\r//' /entrypoint.sh \
    # && sed -i 's/\r//' /gunicorn.sh \
    # && chmod +x /entrypoint.sh \
    # && chown django /entrypoint.sh \
    # && chmod +x /gunicorn.sh \
    # && chown django /gunicorn.sh

COPY . /app

# RUN chown -R django /app

# USER django

EXPOSE 8000

WORKDIR /app/metube

ENTRYPOINT ["/usr/local/bin/gunicorn","-b","127.0.0.1:8000","metube.wsgi:application"]