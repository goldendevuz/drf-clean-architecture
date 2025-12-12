# coding: utf-8

from src.infrastructure.settings.base import *
from src.infrastructure.settings.config import DATABASES, REDIS_URL

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = DATABASES

# Cache
# https://docs.djangoproject.com/en/3.2/topics/cache/

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        "LOCATION": REDIS_URL,
        'TIMEOUT': 60 * 60 * 24,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'SOCKET_CONNECT_TIMEOUT': 5,
            'SOCKET_TIMEOUT': 5,
        }
    }
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Forex - Django Clean Architecture',
    "DESCRIPTION": "Clean Architecture approach for Django project code structure implementation.",
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'COMPONENT_SPLIT_REQUEST':True,
    'SCHEMA_PATH_PREFIX': r'/api/',  # Example: /api/users will get 'users' tag,
}