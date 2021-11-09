import os
from .base import *

DEBUG = False

CORS_ALLOWED_ORIGINS = os.environ.get("CORS_ALLOWED_ORIGINS")

ADMIN_URL = os.environ.get("ADMIN_URL")

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
