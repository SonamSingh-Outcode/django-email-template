# SECURITY
# ------------------------------------------------------------------------------
from config.settings import ENABLE_SECURE_SITE

if ENABLE_SECURE_SITE is True:
    # Security (SSL)
    SESSION_COOKIE_SECURE = True
    DJANGO_SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_HSTS_SECONDS = 63072000  # 2 years
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_SSL_REDIRECT = True
    SECURE_REFERRER_POLICY = 'same-origin'
    CSRF_COOKIE_SECURE = True

    # Other secure headers
    USE_X_FORWARDED_HOST = True
    X_FRAME_OPTIONS = 'DENY'
