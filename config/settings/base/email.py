from decouple import config

# Email Settings
EMAIL_BACKEND = config("EMAIL_BACKEND", default='django.core.mail.backends.console.EmailBackend')

FROM_EMAIL = config('FROM_EMAIL')

EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587)
EMAIL_USE_TLS = True
EMAIL_TIMEOUT = 5

EMAIL_SUBJECT_PREFIX = "[app]"
