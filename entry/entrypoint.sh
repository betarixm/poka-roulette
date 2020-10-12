#!/usr/bin/env bash

python manage.py migrate --noinput
python manage.py collectstatic --noinput
gunicorn app.wsgi -b 0.0.0.0:8080
