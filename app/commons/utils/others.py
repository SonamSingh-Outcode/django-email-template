from decouple import config


def get_http_protocol():
    protol = 'https' if config('ENABLE_SECURE_SITE') is True else 'http'
    return protol
