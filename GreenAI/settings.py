"""
Django settings for GreenAI project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# --------------------------------------------------------------------------------------
# Paths & .env
# --------------------------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")  # load local .env during dev

# --------------------------------------------------------------------------------------
# Security & core config
# --------------------------------------------------------------------------------------
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
SECRET_KEY = os.getenv("SECRET_KEY", "CHANGE-ME-DEV-ONLY")

# Local defaults; add your Render host(s) via env in production
ALLOWED_HOSTS = os.getenv(
    "ALLOWED_HOSTS",
    "localhost,127.0.0.1"
).split(",")

# For forms/admin on Render; you can add your exact Render URL via env
CSRF_TRUSTED_ORIGINS = ["https://*.onrender.com"]
_extra_csrf = os.getenv("CSRF_TRUSTED_ORIGINS_EXTRA", "")
if _extra_csrf:
    CSRF_TRUSTED_ORIGINS += [o.strip() for o in _extra_csrf.split(",") if o.strip()]

# Trust proxy headers on Render
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

# --------------------------------------------------------------------------------------
# Applications
# --------------------------------------------------------------------------------------
INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "website",
    "tinymce",
]

# --------------------------------------------------------------------------------------
# Middleware (WhiteNoise after SecurityMiddleware)
# --------------------------------------------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # serves /static/ in prod
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "GreenAI.urls"

# --------------------------------------------------------------------------------------
# Templates
# --------------------------------------------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],  # optional; keep if you have a templates/ dir
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "website.context_processors.footer_gallery_images",
                "website.context_processors.subscribe_form",
            ],
        },
    },
]

WSGI_APPLICATION = "GreenAI.wsgi.application"

# --------------------------------------------------------------------------------------
# Database (SQLite by default; switch to Postgres via env later if needed)
# --------------------------------------------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# --------------------------------------------------------------------------------------
# Password validation
# --------------------------------------------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# --------------------------------------------------------------------------------------
# Internationalization
# --------------------------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Africa/Nairobi"
USE_I18N = True
USE_TZ = True

# --------------------------------------------------------------------------------------
# Static files (CSS/JS) – WhiteNoise
# --------------------------------------------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"                 # collectstatic target
STATICFILES_DIRS = [BASE_DIR / "website" / "static"]   # your source assets

# Hashed & compressed static files for proper caching + MIME types
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Let collectstatic continue even if a CSS url(...) target can't be found (clean up later)
WHITENOISE_MANIFEST_STRICT = False

# --------------------------------------------------------------------------------------
# Media (admin uploads)
# --------------------------------------------------------------------------------------
MEDIA_URL = "/media/"
# On Render, set MEDIA_ROOT=/var/media (with a mounted Disk). Locally it defaults to <project>/media
MEDIA_ROOT = os.getenv("MEDIA_ROOT", str(BASE_DIR / "media"))

# --------------------------------------------------------------------------------------
# Django defaults
# --------------------------------------------------------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
LOGOUT_REDIRECT_URL = "/"

# --------------------------------------------------------------------------------------
# reCAPTCHA (move real keys to env)
# --------------------------------------------------------------------------------------
RECAPTCHA_PUBLIC_KEY = os.getenv("RECAPTCHA_PUBLIC_KEY", "")
RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY", "")

# --------------------------------------------------------------------------------------
# TinyMCE
# --------------------------------------------------------------------------------------
TINYMCE_DEFAULT_CONFIG = {
    "height": 360,
    "width": 800,
    "cleanup_on_startup": True,
    "custom_undo_redo_levels": 20,
    "selector": "textarea",
    "theme": "silver",
    "plugins": """
        textcolor save link image media preview codesample contextmenu
        table code lists fullscreen insertdatetime nonbreaking
        contextmenu directionality searchreplace wordcount visualblocks
        visualchars code fullscreen autolink lists charmap print hr
        anchor pagebreak
    """,
    "toolbar1": """
        fullscreen preview bold italic underline | fontselect
        fontsizeselect | forecolor backcolor | alignleft alignright |
        aligncenter alignjustify | indent outdent | bullist numlist table |
        | link image media | codesample |
    """,
    "toolbar2": "visualblocks visualchars | charmap hr pagebreak nonbreaking anchor | code |",
    "contextmenu": "formats | link image",
    "menubar": True,
    "statusbar": True,
}

# --------------------------------------------------------------------------------------
# Email (use env; never hardcode passwords)
# --------------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "")
