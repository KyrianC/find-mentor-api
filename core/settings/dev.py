from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGIN = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ADMIN_URL = "admin/"

INTERNAL_IPS = ["127.0.0.1", "localhost"]
