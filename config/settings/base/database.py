import sys
from decouple import config

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default="postgres"),
        'USER': config('DB_USER', default="postgres"),
        'PASSWORD': config('DB_PASSWORD', default="password"),
        'HOST': config('DB_HOST', default="localhost"),
        'PORT': config('DB_PORT', default=5432),
        'OPTIONS': {
            'options': '-c search_path=%s' % config('DB_SCHEMA', default='public')
        }
    }
}

DATABASES["default"]["ATOMIC_REQUESTS"] = True
DATABASES["default"]["CONN_MAX_AGE"] = config("CONN_MAX_AGE", default=60, cast=int)
