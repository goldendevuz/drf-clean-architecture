# coding: utf-8

from src.infrastructure.settings.base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
}