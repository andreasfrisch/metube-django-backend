#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate

python manage.py test
