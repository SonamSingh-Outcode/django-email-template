import datetime

import requests


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def get_location_detail(ip):
    detail = requests.get(f'https://ipinfo.io/{ip}/json', timeout=5)
    if detail.status_code == 200:
        data = detail.json()
        if not data.get('country'):
            return None
        return {
            'country': data.get('country'),
            'city': data.get('city')
        }


def get_browser_detail(request):
    user_ip = get_ip(request)
    browser = request.META['HTTP_USER_AGENT']
    response = {'IP_ADDRESS': user_ip,
                'BROWSER': browser,
                'TIME': datetime.datetime.utcnow().strftime('%m/%d/%Y, %H:%M:%S') + ' UTC'
                }
    ip_info = get_location_detail(user_ip)
    if ip_info:
        response.update(ip_info)
    return response
