import os
from pathlib import Path
from decouple import config, Csv
import dj_database_url

# ----------------------------
# Base & .env check
# ----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

env_file_path = BASE_DIR / "core" / ".env"
if not env_file_path.exists():
    print(f".env file not found at {env_file_path}")
    print("Copy .env.example and adjust it to your environment.")
    exit(1)

# ----------------------------
# Django general settings
# ----------------------------
SECRET_KEY = config('SECRET_KEY', default='djangorestframework')
DEBUG = config('DEBUG', default=True, cast=bool)
ADMIN_URL = config('ADMIN_URL', default='admin/')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://127.0.0.1', cast=Csv())
CORS_ALLOWED_ORIGINS = config('CORS_ALLOWED_ORIGINS', default='http://127.0.0.1', cast=Csv())
SWAGGER_URL = config('SWAGGER_URL', default='swagger/')
REDOC_URL = config('REDOC_URL', default='redoc/')
TIME_ZONE = config("TIME_ZONE", default='UTC')
HOST = config("HOST", default='localhost')

# ----------------------------
# Database configuration
# ----------------------------
# Default SQLite names
DB_NAME = config("DB_NAME", default="db.sqlite3")
TEST_DB_NAME = config("TEST_DB_NAME", default="test_db.sqlite3")

# Universal database URL
DATABASE_URL = config(
    "DATABASE_URL",
    default=f"sqlite:///{BASE_DIR / DB_NAME}"
)
parsed_db = dj_database_url.parse(DATABASE_URL)

# Engine handling
if "postgres" in parsed_db.get("ENGINE", ""):
    parsed_db["ENGINE"] = "django.db.backends.postgresql"
    parsed_db["CONN_MAX_AGE"] = config("CONN_MAX_AGE", default=0, cast=int)
else:
    parsed_db["ENGINE"] = "django.db.backends.sqlite3"
    parsed_db["NAME"] = parsed_db.get("NAME", str(BASE_DIR / DB_NAME))

# Test database
parsed_db["TEST"] = {
    "NAME": config("TEST_DATABASE_URL", default=str(BASE_DIR / TEST_DB_NAME))
}

DATABASES = {"default": parsed_db}

# ----------------------------
# Redis & Celery configuration
# ----------------------------
REDIS_URL = config("REDIS_URL", default='redis://redis:6379/0')
CELERY_BROKER_URL = config("CELERY_BROKER_URL", default=REDIS_URL)
CELERY_RESULT_BACKEND = config("CELERY_RESULT_BACKEND", default=REDIS_URL)