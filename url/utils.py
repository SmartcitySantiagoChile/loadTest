from decouple import config

DOMAIN_PREFIX = ''
URL_API_PREFIX = 'esapi'


def format_url(url_path):
    if DOMAIN_PREFIX != '':
        url_path.insert(0, DOMAIN_PREFIX)
    return '/{0}/'.format('/'.join(url_path))


class Login:

    def __init__(self):
        pass

    @property
    def login_url(self):
        return format_url(['user', 'login'])

    @property
    def login_parameters(self):
        return dict(username=config('USERNAME'), password=config('PASSWORD'))
