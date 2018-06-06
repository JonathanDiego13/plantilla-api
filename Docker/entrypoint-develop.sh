#!/bin/bash
echo "python migrations";
python manage.py migrate;
python manage.py collectstatic --noinput;

echo "gunicorn logs";
cd /code;

if [ ! -f logs/gunicorn.access.logs ]; then
    touch logs/gunicorn.access.logs;
fi
if [ ! -f logs/gunicorn.access.logs ]; then
    touch logs/gunicorn.error.logs;
fi

echo "starting gunicorn"
cd web;
exec newrelic-admin run-program gunicorn -c gunicorn.conf.py config.wsgi.develop:application
