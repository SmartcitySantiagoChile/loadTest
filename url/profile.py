import random
from datetime import datetime, timedelta

from url.utils import URL_API_PREFIX, format_url


class Profile:
    def __init__(self):
        self.__url_html_prefix = 'profile'

    @property
    def index(self):
        return format_url([self.__url_html_prefix])

    """
    HTML CALLS
    """

    @property
    def expedition_url(self):
        return format_url([self.__url_html_prefix, 'expedition'])

    @property
    def stop_url(self):
        return format_url([self.__url_html_prefix, 'stop'])

    @property
    def trajectory_url(self):
        return format_url([self.__url_html_prefix, 'trajectory'])

    @property
    def available_days_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableDays'])

    @property
    def available_routes_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableRoutes'])

    @property
    def expedition_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByExpeditionData'])

    @property
    def stop_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByStopData'])

    @property
    def trajectory_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByTrajectoryData'])

    """
    DATA CALLS
    """

    def get_expedition_data_params(self):
        start_date = datetime(2018, 3, 1)
        end_date = start_date + timedelta(days=random.randint(30, 120))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }

    def get_stop_data_params(self):
        start_date = datetime(2018, 3, 1)
        end_date = start_date + timedelta(days=random.randint(30, 120))
        stop_code_list = ['PA433', 'PI61', 'PA347']
        stop_code = stop_code_list[random.randint(0, len(stop_code_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'stopCode': stop_code
        }

    def get_trajectory_data_params(self):
        day = random.randint(1, 27)
        date = datetime(2018, 3, day)
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(date),
            'endDate': str(date),
            'authRoute': auth_route
        }
