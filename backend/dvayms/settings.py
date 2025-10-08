from pathlib import Path
import environ
import os

# --- Paths (repo root -> backend/frontend) ---
REPO_DIR = Path(__file__).resolve().parent.parent.parent  # .../dvayms
BASE_DIR = REPO_DIR / "backend"                           # donde está manage.py
FRONTEND_DIR = REPO_DIR / "frontend"

# --- Env ---
env = environ.Env(
    DJANGO_DEBUG=(bool, True),
    DJANGO_SECRET_KEY=(str, "change-me"),
    DJANGO_ALLOWED_HOSTS=(str, "localhost,127.0.0.1"),
    DB_NAME=(str, "dvayms_db"),
    DB_USER=(str, "dvayms_user"),
    DB_PASSWORD=(str, "dvayms_pass"),
    DB_HOST=(str, "127.0.0.1"),
    DB_PORT=(str, "5432"),
)
environ.Env.read_env(REPO_DIR / ".env")

# --- Core ---
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env("DJANGO_DEBUG")
ALLOWED_HOSTS = [h.strip() for h in env("DJANGO_ALLOWED_HOSTS").split(",")]

# --- Apps ---
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Agregarás apps propias luego: "core", "catalog", "sales", "reports", "common"
]

# --- Middleware ---
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # sirve estáticos en prod/dev
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "dvayms.urls"

# --- Templates (frontend fuera del backend) ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [FRONTEND_DIR / "templates"],  # <— templates globales
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "dvayms.wsgi.application"

# --- Database (Postgres por .env) ---
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": env("DB_NAME"),
        "USER": env("DB_USER"),
        "PASSWORD": env("DB_PASSWORD"),
        "HOST": env("DB_HOST"),
        "PORT": env("DB_PORT"),
    }
}

# --- Passwords ---
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --- I18N ---
LANGUAGE_CODE = "es-ar"
TIME_ZONE = "America/Argentina/Buenos_Aires"
USE_I18N = True
USE_TZ = True

# --- Static files (ubicados en /frontend/static) ---
STATIC_URL = "/static/"
STATICFILES_DIRS = [FRONTEND_DIR / "static"]
STATIC_ROOT = REPO_DIR / "staticfiles"  # para collectstatic
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --- Default PK ---
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# --- Login redirects (funcionará cuando agreguemos auth) ---
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard"
LOGOUT_REDIRECT_URL = "login"
