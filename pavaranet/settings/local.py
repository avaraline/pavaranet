"""
Development Django settings for pavaranet project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from os.path import join, normpath

from .base import *


# Debug configuration.

DEBUG = True

TEMPLATE_DEBUG = DEBUG

INTERNAL_IPS = ('127.0.0.1',)


# Email configuration.

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Database configuration.

DATABASES['default'].update({
    'USER': 'pavaranet',
    'PASSWORD': '',
})


# Cache configuration.

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': SITE_NAME
    }
}


# Add django-debug-toolbar.

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

DEBUG_TOOLBAR_PATCH_SETTINGS = False
