import os


DEBUG = False
STATIC_ROOT = os.getenv("DJANGO_STATIC_ROOT")
STATIC_URL = "/static/"

ALLOWED_HOSTS = ["*"]

# cors configuration
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    os.getenv("FRONT_HOST"),
]

# Media files (Images)
MEDIA_ROOT = os.getenv("DJANGO_MEDIA_ROOT", "/var/wwww/media")
MEDIA_URL = "/media/"

# Postgre DB conf
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("POSTGRES_HOST", "db"),
        "NAME": "estiam_db",
        "USER": "postgres",
        "PASSWORD": "8Fny?aXEFkh9ePA3",
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }
}
