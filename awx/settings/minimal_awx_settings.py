# awx/settings/minimal_awx_settings.py
from awx.settings.defaults import *

# Required for minimal build
SKIP_PRODUCTION_CHECKS = True
INSTALLED_APPS = ['awx.main']  # minimum needed
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
AWX_IS_K8S = False
DEBUG = True

# Add anything else referenced by default_settings
DEFAULTS_SNAPSHOT = {}  # this is mandatory
