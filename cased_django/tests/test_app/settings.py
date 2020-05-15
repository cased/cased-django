import os

DB_NAME = os.path.abspath(os.path.dirname(__name__)) + "/cased_test_db"

CASED_PUBLISH_KEY = "test-key-123"
CASED_API_BASE = "https://api.example.com"
CASED_PUBLISH_BASE = "https://publish.example.com"
CASED_DISABLE_PUBLISHING = True
CASED_RELIABILITY_BACKEND = "redis"
SECRET_KEY = "test-key"
CASED_SENSITIVE_FIELDS = {"email_address"}
CASED_LOG_LEVEL = "INFO"
CASED_INCLUDE_IP_ADDRESS = True

AUTH_USER_MODEL = "auth.User"

INSTALLED_APPS = [
    "test_app",
    "cased_django",
    "django.contrib.auth",
    "django.contrib.contenttypes",
]

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": DB_NAME}}


MIDDLEWARE_CLASSES = [
    "cased_django.CasedIpMiddleware",
]
