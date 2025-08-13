from awx.settings.default import *

SECRET_KEY = 'dummy'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/tmp/awx.db',
    }
}
