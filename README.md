[![Build Status](https://travis-ci.org/EnviroMonitor/EnviroMonitorWeb.svg?branch=master)](https://travis-ci.org/EnviroMonitor/EnviroMonitorWeb)

# EnviroMonitorWeb
API and simple web interface for EnviroMonitor project. Powered by Django

EnviroMonitorWeb provides backend API to which your air quality sensors can send data. It also provides monitoring station management, user management and simple frontend to present data. You can use this project to start awareness campaing in you local area.

# Development with Docker and docker-compose
You can up and runnig this project in a traditional way with virtual environment + postgis config, but it much easier to run it using docker.

## To start development:
1. install [docker](https://docs.docker.com/#/components) and [docker-compose](https://docs.docker.com/compose/install/)
2. clone and change working dir to project root `cd ~/ && git clone git@github.com:EnviroMonitor/EnviroMonitorWeb.git && cd EnviroMonitorWeb`
3. copy/symlink docker-compose.yml `cp ./docker/docker-compose.yml ./docker-compose.yml` (we want to be able to override as dev)
4. run `docker-compose build` to build web container
5. run `docker-compose run --rm web python manage.py migrate`
6. run `docker-compose run --rm web python manage.py createsuperuser`

## To run project:
1. docker-compose up
2. point Your browser to `localhost:8000`
3. press `CTRL+C` to stop

## Notes:
1. To run command inside container you can use run entrypoint command. 
I.e. `docker-compose run --rm web py.test -s --cov=. --cov-report=html` to run unit tests and check coverage.

## API documentaion:
Check http://localhost:8000/api/v1/docs/ to received full REST API documentation.
