from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test-secret-key"
DEBUG = True
ALLOWED_HOSTS = ["*"]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "simple_history",
    "captcha",
    "django_starter_core.contrib.about",
    "django_starter_core.contrib.admin",
    "django_starter_core.contrib.auth",
    "django_starter_core.contrib.config",
    "django_starter_core.contrib.docs",
    "django_starter_core.contrib.forms",
    "django_starter_core.contrib.guide",
    "django_starter_core.contrib.monitoring",
    "django_starter_core.contrib.navbar",
    "django_starter_core.contrib.notifications",
    "django_starter_core.contrib.seed",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "tests.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"

DJANGO_STARTER = {
    "auth": {
        "jwt": {
            "algo": "HS256",
            "salt": "test-salt-test-salt-test-salt-test-salt",
            "lifetime": 3600,
        }
    },
    "admin": {
        "site_header": "DjangoStarter",
        "site_title": "DjangoStarter",
        "index_title": "DjangoStarter",
        "list_per_page": 20,
    },
    "site": {
        "enable_contact_form": True,
    },
}
