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
    def expedition(self):
        return format_url([self.__url_html_prefix, 'expedition'])

    @property
    def stop(self):
        return format_url([self.__url_html_prefix, 'stop'])

    @property
    def trajectory(self):
        return format_url([self.__url_html_prefix, 'trajectory'])

    @property
    def expedition_data_url(self):
        params = '?{0}'.format()
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'loadProfileByExpeditionData' + params])

    """
    DATA CALLS
    """

    @property
    def expedition_data_params(self):
        start_date = datetime(2017, 5, 8)
        end_date = start_date + timedelta(days=random.randint(0, 6))
        auth_route_list = ['T101 00I', 'T505 00I', 'T517 00I']
        auth_route = auth_route_list[random.randint(0, len(auth_route_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'authRoute': auth_route
        }
