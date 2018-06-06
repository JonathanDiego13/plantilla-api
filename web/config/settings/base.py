import os
import sys

from corsheaders.defaults import default_headers

# root of the project
root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
BASE_DIR = root
SITE_ROOT = root

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))  # add apps directory to sys path

ADMINS = (
    ('Alvaro Burgos', 'alvaro.burgos@luuna.mx '),
    ('Steve Ludwig', 'steve.beltran@luuna.mx'),
)

DEFAULT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = ['rest_framework', 'corsheaders']

USER_DEFINED_APPS = []

RENDERER_CLASSES = (
    'rest_framework.renderers.JSONRenderer',
) if os.environ.get('ENV_MODE') == 'production' else (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAdminUser',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': RENDERER_CLASSES,
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# custom user model
AUTH_USER_MODEL = 'user.User'

AUTH_PASSWORD_VALIDATORS = [
    {  # shouldn't be similar to user's attributes
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {  # should be longer than 7 characters
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {  # shouldn't be common
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {  # shouldn't be numeric
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Hashing algorithm
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

# translation and formatting
USE_I18N = True
USE_L10N = True

# use local time zone instead of UTC
USE_TZ = False

# language code and local timezone
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE', 'es-mx')
DEFAULT_CHARSET = 'utf-8'
TIME_ZONE = os.environ.get('TIME_ZONE', 'America/Mexico_City')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# CORS - Cross origin resource sharing
CORS_ALLOW_HEADERS = default_headers + ('token',)
