# -*- coding: utf-8 -*-
import random
from datetime import datetime, timedelta

from url.utils import URL_API_PREFIX, format_url

class Trip:

    def __init__(self):
        self.__url_html_prefix = 'trip'
        self.start_date = datetime(2017, 7, 31)
        self.delta = 37

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
    def resume_url(self):
        return format_url([self.__url_html_prefix, 'resume'])

    @property
    def map_url(self):
        return format_url([self.__url_html_prefix, 'map'])

    @property
    def large_trips_url(self):
        return format_url([self.__url_html_prefix, 'large-trips'])

    @property
    def from_to_map_url(self):
        return format_url([self.__url_html_prefix, 'fromToMaps'])

    @property
    def strategies_url(self):
        return format_url([self.__url_html_prefix, 'strategies'])

    @property
    def available_days_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'availableDays'])

    @property
    def transfer_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'transfersData'])

    @property
    def resume_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'resumeData'])

    @property
    def map_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'mapData'])

    @property
    def large_trips_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'largeTravelData'])

    @property
    def from_to_map_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'fromToMapData'])

    @property
    def strategies_data_url(self):
        return format_url([URL_API_PREFIX, self.__url_html_prefix, 'strategiesData'])

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

    def get_resume_data_params(self):
        end_date = self.start_date + timedelta(days=random.randint(2, self.delta))

        return {
            'startDate': str(self.start_date),
            'endDate': str(end_date),
        }

    def get_map_data_params(self):
        end_date = self.start_date + timedelta(days=random.randint(2, self.delta))

        return {
            'startDate': str(self.start_date),
            'endDate': str(end_date),
        }

    def get_large_trips_data_params(self):
        end_date = self.start_date + timedelta(days=random.randint(2, self.delta))
        stages = random.sample([1, 2, 3, 4, '5+'], random.randint(1, 5))
        origin_or_destination = random.choice(['origin', 'destination'])

        return {
            'startDate': str(self.start_date),
            'endDate': str(end_date),
            'stages': stages,
            'originOrDestination': origin_or_destination
        }

    def get_from_to_map_data_params(self):
        end_date = self.start_date + timedelta(days=random.randint(2, self.delta))
        stages = random.sample([1, 2, 3, 4], random.randint(1, 4))
        transport_modes = random.sample([1, 2, 3, 4, 5, 6, 7], random.randint(1, 7))

        return {
            'startDate': str(self.start_date),
            'endDate': str(end_date),
            'stages': stages,
            'transportModes': transport_modes
        }

    def get_strategies_data_params(self):
        end_date = self.start_date + timedelta(days=random.randint(2, self.delta))
        zones = range(1, 800)
        origin_zones = random.sample(zones, random.randint(1, 20))
        destination_zones = random.sample(zones, random.randint(1, 20))

        return {
            'startDate': str(self.start_date),
            'endDate': str(end_date),
            'originZones': origin_zones,
            'destinationZones': destination_zones
        }