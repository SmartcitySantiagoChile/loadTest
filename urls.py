# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
from datetime import datetime, timedelta

"""
This file contains url to be used by locust
"""
DOMAIN_PREFIX = 'fondefviz'
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
        return format_url(['login'])

    @property
    def login_parameters(self):
        return {
            'id_username': 'transantiago',
            'id_password': 'transantiago'
        }


class ODByRoute:
    def __init__(self):
        self.__url_html_prefix = 'odbyroute'

    @property
    def matrix_url(self):
        return format_url(['profile', 'odmatrix'])

    @property
    def matrix_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'matrixData'])

    def get_matrix_data_params(self):
        start_date = datetime(2017, 4, 4)
        end_date = start_date + timedelta(days=random.randint(90, 130))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }


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
    def expedition_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByExpeditionData'])

    @property
    def stop_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByStopData'])

    """
    DATA CALLS
    """

    def get_expedition_data_params(self):
        start_date = datetime(2017, 5, 8)
        end_date = start_date + timedelta(days=random.randint(30, 120))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }

    def get_stop_data_params(self):
        start_date = datetime(2017, 5, 8)
        end_date = start_date + timedelta(days=random.randint(30, 120))
        stop_code_list = ['PA433', 'PI61', 'PA347']
        stop_code = stop_code_list[random.randint(0, len(stop_code_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'stopCode': stop_code
        }


class Speed:

    def __init__(self):
        self.__url_html_prefix = 'speed'

    @property
    def index(self):
        return format_url([self.__url_html_prefix])

    """
    HTML CALLS
    """

    @property
    def matrix_url(self):
        return format_url([self.__url_html_prefix, 'matrix'])

    @property
    def ranking_url(self):
        return format_url([self.__url_html_prefix, 'ranking'])

    @property
    def variation_url(self):
        return format_url([self.__url_html_prefix, 'variation'])

    @property
    def matrix_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'matrixData'])

    @property
    def ranking_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'rankingData'])

    @property
    def variation_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'speedVariation'])

    """
    DATA CALLS
    """

    def get_matrix_data_params(self):
        start_date = datetime(2017, 3, 1)
        end_date = start_date + timedelta(days=random.randint(200, 300))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }

    def get_ranking_data_params(self):
        start_date = datetime(2017, 3, 1)
        end_date = start_date + timedelta(days=random.randint(200, 300))

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'hourPeriodFrom': 0,
            'hourPeriodTo': 23
        }

    def get_variation_data_params(self):
        base_date = datetime(2017, 3, 1)
        start_date = base_date + timedelta(days=random.randint(200, 300))
        operator = random.randint(1, 7)

        return {
            'startDate': str(start_date),
            'operator': operator,
        }
