![Build Status](https://travis-ci.org/EnviroMonitor/EnviroMonitorWeb.svg?branch=master)

# EnviroMonitorWeb

API and simple web interface for EnviroMonitor project. Powered by Django

EnviroMonitorWeb provides backend API to which your air quality sensors can send data. It also provides monitoring station management, user management and simple frontend to present data. You can use this project to start awareness campaing in you local area.

# Development and deployment with Docker
You can up and runnig this project in a traditional way with virtual environment but you can also use power of docker and docker-compose.
Dockerfile is using python 3.5 image.

## To build project with docker-compose follow below steps:
1. docker-compose build web
2. docker-compose run web python manage.py migrate
3. docker-compose run web python manage.py createsuperuser

## To run project with docker-compose:
1. docker-compose up web

## API documentaion.
For this project we have endpoint /docs with automatically generated documentation to REST API
I.e. if you are using docker you can hit http://0.0.0.0:8000/docs/ to received full REST API documentation.