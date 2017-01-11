#!/bin/sh
set -e

cd /code/

if [ "$1" = 'runserver' ]; then
    exec python manage.py runserver 0.0.0.0:8000
elif [ "$1" = 'managepy' ]; then
    exec python manage.py
elif [ "$1" = 'run' ]; then
    # exec all but fist argument
    # http://stackoverflow.com/a/9057699/479931
    shift
    exec "${@}"
else
    exec python manage.py "$@"
fi
