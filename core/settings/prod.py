import os
from .base import *

DEBUG = False

ADMIN_URL = os.environ.get("ADMIN_URL")

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
