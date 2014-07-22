"""
Common Django settings for pavaranet project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""


from os.path import abspath, dirname, join, normpath, split


# Build paths inside the project like this: join(BASE_DIR, ...)
PROJECT_DIR = dirname(dirname(abspath(__file__)))

BASE_DIR, SITE_NAME = split(PROJECT_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '4^0rz@mqs^u6(!8($zohp%$1ky*)_7cn5jq47hmx%a9*1gt)%b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []


# Application definition

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

LOCAL_APPS = (
    'pavaranet.social',
    'pavaranet.stats',
)

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = '{0}.urls'.format(SITE_NAME)

WSGI_APPLICATION = '{0}.wsgi.application'.format(SITE_NAME)

AUTH_USER_MODEL = 'social.Player'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': SITE_NAME,
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/

STATIC_ROOT = normpath(join(BASE_DIR, 'static'))

STATIC_URL = '/static/'


# Media files (user-uploaded file store)
# https://docs.djangoproject.com/en/dev/topics/files/

MEDIA_ROOT = normpath(join(BASE_DIR, 'assets'))

MEDIA_URL = '/assets/'


# pavaranet settings
# These can be tweaked in the future if we need to run multiple installations,
# e.g. breaking the players up by region or language.

PAVARANET_CLAN_NAME_MAX_LENGTH = 30
PAVARANET_CLAN_TAG_MAX_LENGTH = 6
PAVARANET_HANDLE_MAX_LENGTH = 20
PAVARANET_HANDLE_CODE_RANGE = range(1000, 2000)
PAVARANET_NAMING_REGEX = r'^[A-Z][A-Z0-9\ ]{2,}$'
PAVARANET_NAMING_ERROR = ('Names and handles must consist of letters, numbers, '
                          'and spaces, begin with a letter, and be at least 3 '
                          'characters long.')
PAVARANET_NAMING_BANNED_WORDS = (r'fart', r'poop') # Who wants to commit THIS?
