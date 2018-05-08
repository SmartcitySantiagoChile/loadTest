# -*- coding: utf-8 -*-
from locust import TaskSet, task

from url.trip import Trip


class TripUserBehavior(TaskSet):

    def __init__(self, parent):
        super(TripUserBehavior, self).__init__(parent)
        self.trip_url = Trip()
        self.only_data = True

    @task(10)
    def resume(self):
        if not self.only_data:
            self.client.get(self.trip_url.resume_url)
            self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.resume_data_url, params=self.trip_url.get_resume_data_params(),
                        name=self.trip_url.resume_data_url)

    @task(10)
    def map(self):
        if not self.only_data:
            self.client.get(self.trip_url.map_url)
            self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.map_data_url, params=self.trip_url.get_map_data_params(),
                        name=self.trip_url.map_data_url)

    @task(10)
    def large_trips(self):
        if not self.only_data:
            self.client.get(self.trip_url.large_trips_url)
            self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.large_trips_data_url, params=self.trip_url.get_large_trips_data_params(),
                        name=self.trip_url.large_trips_data_url)

    @task(10)
    def from_to_maps(self):
        if not self.only_data:
            self.client.get(self.trip_url.from_to_map_url)
            self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.from_to_map_data_url, params=self.trip_url.get_from_to_map_data_params(),
                        name=self.trip_url.from_to_map_data_url)

    @task(10)
    def strategies(self):
        if not self.only_data:
            self.client.get(self.trip_url.strategies_url)
            self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.strategies_data_url, params=self.trip_url.get_strategies_data_params(),
                        name=self.trip_url.strategies_data_url)

    @task(50)
    def stop(self):
        self.interrupt()
