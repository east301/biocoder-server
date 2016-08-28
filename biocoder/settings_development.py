#
# (c) 2016 biocoder developers
#
# This file is part of biocoder,
# released under Apache License Version 2.0 (http://www.apache.org/licenses/LICENCE).
#

import os

import redislite

from .settings_common import *  # NOQA


# ================================================================================
# project path
# ================================================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# ================================================================================
# security
# ================================================================================

SECRET_KEY = '_+tfbe3v%p^i+w)2-pnuyv9w=ij=2jit(&_h%b)g24(1^r_x*0'

DEBUG = True
ALLOWED_HOSTS = []


# ================================================================================
# Applications & middlewares
# ================================================================================

INSTALLED_APPS += [
    'django.contrib.admin',
    'debug_toolbar'
]

MIDDLEWARE = [
    'biocoder.apps.common.debug.DebugToolbarMiddleware'
] + MIDDLEWARE


# ================================================================================
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# ================================================================================

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'temporary', 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'temporary', 'media')


# ================================================================================
# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# ================================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'temporary', 'db.sqlite3')
    }
}


# ================================================================================
# Redis
# ================================================================================

REDIS_PORT = int(os.environ.get('DJANGO_REDIS_PORT', '8001'))
REDIS = redislite.Redis(
    os.path.join(BASE_DIR, 'temporary', 'celery.rdb'),
    serverconfig={'port': str(REDIS_PORT)})


# ================================================================================
# Channels
# ================================================================================

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'asgi_redis.RedisChannelLayer',
        'ROUTING': 'biocoder.routing.channel_routing',
        'CONFIG': [
            'redis://127.0.0.1:{}/0'.format(REDIS_PORT)
        ]
    }
}


# ================================================================================
# Celery
# ================================================================================

BROKER_URL = 'redis://127.0.0.1:{}/1'.format(REDIS_PORT)
CELERY_RESULT_BACKEND = BROKER_URL
