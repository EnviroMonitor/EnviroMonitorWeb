#!/bin/sh

# wait for postgis to start
/wait-for-it.sh postgis:5432

"${@}"

# change owner of files after running command
# eg. python manage.py makemigrations
# ommit ./docker/ directory
find /code/ -user root 2>/dev/null | grep -v './docker' | tr "\n" "\0" | xargs -r0 chown ${DEFAULT_UID}:${DEFAULT_GID}
