import os
from pathlib import Path


# Logging
BASE_LOG_DIR = os.path.join(Path(__file__).parents[4], 'logs')


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d:\n\t %(message)s \n',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s\n\t %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'info_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'django.info.log'),
            'maxBytes': 5242880,  # 5MB
            'backupCount': 1,
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
        'debug_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_LOG_DIR, 'django.debug.log'),
            'maxBytes': 5242880,  # 5MB
            'backupCount': 1,
            'formatter': 'simple',
            'filters': ['require_debug_true']
        },
    },
    'loggers': {
        'info_log': {
            'handlers': ['info_handler'],
            'level': 'INFO',
            'propagate': True
        },
        'debug_log': {
            'handlers': ['debug_handler'],
            'level': 'DEBUG',
            'propagate': True
        },
        'error_log': {
            'handlers': ['error_handler'],
            'level': 'ERROR',
            'propagate': True
        },
        'critical_log': {
            'handlers': ['critical_handler'],
            'level': 'CRITICAL',
            'propagate': True
        }
    }
}
