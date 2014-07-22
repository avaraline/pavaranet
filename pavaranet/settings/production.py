"""
Production Django settings for pavaranet project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

from os import environ

from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_setting(setting):
    """
    Get the environment setting or return an exception.
    """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the {0} env variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# Secret configuration.

SECRET_KEY = get_env_setting('SECRET_KEY')


# Host configuration.

ALLOWED_HOSTS = []


# Email configuration.

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

EMAIL_PORT = environ.get('EMAIL_PORT', 587)

EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

EMAIL_USE_TLS = True

SERVER_EMAIL = EMAIL_HOST_USER


# Database configuration.

DATABASES['default'].update({
    'USER': 'pavaranet',
    'PASSWORD': get_env_setting('PAVARANET_DB_PASSWORD'),
})


# Cache configuration.

CACHES = {}
