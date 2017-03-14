"""
WSGI config for EnviroMonitorWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "EnviroMonitorWeb.settings")

application = get_wsgi_application()
