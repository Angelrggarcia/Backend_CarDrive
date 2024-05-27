import os

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

from .base import *
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'database_high',
        'USER': 'ADMIN',
        'PASSWORD': 'Foreverz#115',
        'OPTIONS': {
            "config_dir": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'CarDriveDB')),
            "wallet_location": os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'CarDriveDB')),
            "wallet_password": "Foreverz#115"
        }
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
    