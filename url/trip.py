# -*- coding: utf-8 -*-
import random
from datetime import datetime, timedelta

from url.utils import URL_API_PREFIX, format_url


class Trip:

    def __init__(self):
        self.__url_html_prefix = 'trip'

    @property
    def index(self):
        return format_url([self.__url_html_prefix])

    """
    HTML CALLS
    """

    @property
    def transfer_url(self):
        return format_url(['profile', 'transfers'])

    @property
    def available_days_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableDays'])

    @property
    def transfer_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'transfersData'])

    """
    DATA CALLS
    """

    def get_transfer_data_params(self):
        start_date = datetime(2017, 5, 8)
        end_date = start_date + timedelta(days=random.randint(80, 120))
        stop_code_list = ['PA433', 'PI61', 'PA347']
        stop_code = stop_code_list[random.randint(0, len(stop_code_list) - 1)]

        return {
            'startDate': str(start_date),
            'endDate': str(end_date),
            'stopCode': stop_code
        }
