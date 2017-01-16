FROM python:3.5

ENV PYTHONUNBUFFERED 1
# change owner of all files created during any cmd,
# override them in Yours docker-compose.yml file
ENV DEFAULT_UID=1000
ENV DEFAULT_GID=1000

WORKDIR /code/

# update packages and install apt-reqs
RUN apt-get update && apt-get install -y --no-install-recommends \
   # apt requirements
    ## common
    g++ curl ca-certificates \
   # pip apt requirements
    ## common
    python3-dev \
    ## psycopg2
    postgresql-server-dev-all \
    ## manage.py dbshell
    postgresql-client \
    ## django.contrib.gis
    binutils libproj-dev gdal-bin \
    && rm -rf /var/lib/apt/lists/*

# get newest pip wheel and setuptools
RUN curl https://bootstrap.pypa.io/get-pip.py | python

# add pip dependencies
ADD requirements.txt /
RUN pip install -r /requirements.txt

# add cmd
ADD cmd.sh /
CMD ["/cmd.sh"]

# add entrypoint
ADD wait-for-it.sh /
ADD docker_entrypoint.sh /
ENTRYPOINT ["/docker_entrypoint.sh"]
