log_configuration = {
    'version': 1,
    'disable_existing_loggers': False,
    'style': '{',
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'errorformat': {
            'format': '%(levelname)s %(asctime)s %(pathname)s %(module)s %(process)d %(thread)d %(message)s %(exc_info)s'
        },
        'infoformat': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'error_file_format': {
            'format': '%(levelname)s %(asctime)s %(message)s %(pathname)s %(exc_info)s'
        },
        'securityformat': {
            'format': '%(levelname)s %(asctime)s %(module)s %(message)s'
        },
        'mailformat': {
            'format': '%(levelname)s %(asctime)s %(message)s %(pathname)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'console_warning': {
            'level': 'WARNING',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'console_error': {
            'level': 'ERROR',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'file_info': {
            'level': 'INFO',
            'filters': ['require_debug_false'],
            'class': 'logging.FileHandler',
            'filename': 'general.log',
            'formatter': 'infoformat',
        },
        'file_error': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'error.log',
            'formatter': 'error_file_format',
        },
        'file_security': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
            'formatter': 'securityformat',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'mailformat',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'console_warning', 'console_error', 'file_info'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['mail_admins', 'file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.template': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db_backends': {
            'handlers': ['file_error'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.security': {
            'handlers': ['file_security'],
            'level': 'INFO',
            'propagate': False,
        }
    }
}
