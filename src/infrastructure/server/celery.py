# coding: utf-8

import os

from celery import Celery
from src.infrastructure.settings.config import DJANGO_ENV


settings_module = f'src.infrastructure.settings.{DJANGO_ENV}'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

app = Celery('forex')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
