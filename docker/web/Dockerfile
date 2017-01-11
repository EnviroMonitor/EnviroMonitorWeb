FROM ubuntu:16.04

ENV PYTHONUNBUFFERED 1

WORKDIR /

# update packages and install apt-reqs
RUN apt-get update && apt-get install -y --no-install-recommends \
   # apt requirements
    ## common
    g++ curl ca-certificates python3 \
   # pip apt requirements
    ## common
    python3-dev \
    ## psycopg2
    postgresql-server-dev-9.5 \
    ## manage.py dbshell
    postgresql-client-9.5 \
    ## django.contrib.gis
    binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# make python3 default python executable
RUN ln -fs /usr/bin/python3 /usr/bin/python

# get newest pip wheel and setuptools
RUN curl https://bootstrap.pypa.io/get-pip.py | python

# add pip dependencies
ADD requirements.txt /
RUN pip install -r /requirements.txt

# add entrypoint
ADD docker_entrypoint.sh /
ENTRYPOINT ["/docker_entrypoint.sh"]

CMD ["runserver"]
