# minimal_awx_settings.py
DEBUG = False
SECRET_KEY = "fake-secret-key-for-build"
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}
