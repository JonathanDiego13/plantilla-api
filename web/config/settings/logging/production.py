from .base import *

LOGGING['handlers'].update({
    'error_handler': {
        'level': 'ERROR',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(BASE_LOG_DIR, 'django.error.log'),
        'maxBytes': 5242880,
        'backupCount': 5,
        'formatter': 'verbose',
    },
    'critical_handler': {
        'level': 'CRITICAL',
        'class': 'logging.handlers.RotatingFileHandler',
        'filename': os.path.join(BASE_LOG_DIR, 'django.critical.log'),
        'maxBytes': 5242880,
        'backupCount': 5,
        'formatter': 'verbose',
    },
    'users_handler': {
        'level': 'ERROR',
        'class': 'django.utils.log.AdminEmailHandler',
        'formatter': 'verbose',
        # 'filters': ['require_debug_false']
    }
})

LOGGING['loggers'].update({
    'users_log': {
        'handlers': ['users_handler', 'error_handler'],
        'level': 'ERROR',
        'propagate': True
    },
})
