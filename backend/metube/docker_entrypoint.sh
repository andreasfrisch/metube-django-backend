#!/bin/sh
python manage.py migrate
python manage.py collectstatic --noinput

# Prepare log files and start outputting logs to stdout
# touch /srv/logs/gunicorn.log
# touch /srv/logs/access.log
# tail -n 0 -f /srv/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn metube.wsgi:application \
    --name metube-django \
    --bind 0.0.0.0:8000 \
    # --log-level=info \
    # --log-file=/srv/logs/gunicorn.log \
    # --access-logfile=/srv/logs/access.log \
    "$@"