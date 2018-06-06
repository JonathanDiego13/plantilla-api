from .base import *
from .logging.develop import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

WSGI_APPLICATION = 'config.wsgi.develop.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT')
    },
}

CORS_ORIGIN_ALLOW_ALL = True

assert SECRET_KEY
assert os.environ.get('BROKER_URL')
assert os.environ.get('REDIS_URL')
assert os.environ.get('BROKER_URL')
assert CORS_ORIGIN_ALLOW_ALL
