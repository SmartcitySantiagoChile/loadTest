# -*- coding: utf-8 -*-
import random
from datetime import datetime, timedelta

from url.utils import URL_API_PREFIX, format_url


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
    def available_days_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableDays'])

    @property
    def available_routes_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableRoutes'])

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
