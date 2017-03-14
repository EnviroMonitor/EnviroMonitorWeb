import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    '.smogly.irynek.pl',
    'smogly.pl',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST')
    }
}
