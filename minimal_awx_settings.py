# minimal_awx_settings.py
# minimal_awx_settings.py
SECRET_KEY = "dev"
DEFAULTS_SNAPSHOT = {}
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "/tmp/awx_dev.sqlite3",
    }
}
