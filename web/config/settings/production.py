from .base import *
from .logging.production import *

SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False

ALLOWED_HOSTS = [
    '*',
]

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + USER_DEFINED_APPS

WSGI_APPLICATION = 'config.wsgi.production.application'

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

CORS_ORIGIN_ALLOW_ALL = True
#CORS_ORIGIN_WHITELIST = (
#    'luuna.mx',
#    'www.luuna.mx',
#)

# HTTPS specific settings.
# redirect to https in case the user comes via http
# SECURE_SSL_REDIRECT = True
# number of seconds for which we want to set this setting in user's browser. should be low otherwise
# an error on part can lock the user out for that many seconds.
# SECURE_HSTS_SECONDS = 300
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # also include the sub-domains
# SECURE_CONTENT_TYPE_NOSNIFF = True  # browsers cannot sniff the content headers (malicious)
# CSRF_COOKIE_SECURE = True  # cookies can be sent only on https
# SESSION_COOKIE_SECURE = True
#
# CSRF_COOKIE_HTTPONLY = True  # cookies can only be accessed in http request.
# SESSION_COOKIE_HTTPONLY = True  # javascript can't access them
#
# X_FRAME_OPTIONS = 'SAMEORIGIN'  # only we can display x-frames
#
# SECURE_BROWSER_XSS_FILTER = True


assert SECRET_KEY
assert os.environ.get('BROKER_URL')
assert os.environ.get('REDIS_URL')
assert os.environ.get('BROKER_URL')
