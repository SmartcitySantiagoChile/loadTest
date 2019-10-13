import random
from datetime import datetime, timedelta

from url.utils import URL_API_PREFIX, format_url


class ODByRoute:
    def __init__(self):
        self.__url_html_prefix = 'odbyroute'

    @property
    def matrix_url(self):
        return format_url(['profile', 'odmatrix'])

    @property
    def available_days_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableDays'])

    @property
    def available_routes_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableRoutes'])

    @property
    def matrix_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'matrixData'])

    def get_matrix_data_params(self):
        start_date = datetime(2018, 3, 1)
        end_date = start_date + timedelta(days=random.randint(90, 130))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }
