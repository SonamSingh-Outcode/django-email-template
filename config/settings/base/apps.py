# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THRID_PARTY_APPS = [
    'corsheaders',
    'cuser',
    'django_filters',
    'drf_yasg',
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist'
]

LOCAL_APPS = [
    'core',
    'app.commons',
    'app.authentications',
    'app.users'
]

INSTALLED_APPS = DJANGO_APPS + THRID_PARTY_APPS + LOCAL_APPS
