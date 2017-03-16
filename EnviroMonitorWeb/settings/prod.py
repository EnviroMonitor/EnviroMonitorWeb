import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = [
    '*',
]

ADMINS = [
    ('Tomasz Napierała', os.environ.get('EMAIL_ZEN')),
    ('Leszek Piątek', os.environ.get('EMAIL_LECHUP')),
    ('Krzysztof Hasiński', os.environ.get('EMAIL_KHASINSKI')),
]

STATIC_ROOT = os.path.join(BASE_DIR, "static-collected")

DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 30

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST')
    }
}
