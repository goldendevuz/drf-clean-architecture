# coding: utf-8

from src.infrastructure.settings.base import *

SPECTACULAR_SETTINGS = {
    'TITLE': 'Ex Forex - Django Clean Architecture',
    "DESCRIPTION": "Clean Architecture approach for Django project code structure implementation.",
    'VERSION': '0.0.1',
    'SERVE_INCLUDE_SCHEMA': False,
    'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    'REDOC_DIST': 'SIDECAR',
    'COMPONENT_SPLIT_REQUEST':True,
    'SCHEMA_PATH_PREFIX': r'/api/',  # Example: /api/users will get 'users' tag,
}