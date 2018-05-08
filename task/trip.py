# -*- coding: utf-8 -*-
from locust import TaskSet, task

from url.trip import Trip


class TripUserBehavior(TaskSet):

    def __init__(self, parent):
        super(TripUserBehavior, self).__init__(parent)
        self.trip_url = Trip()

    @task(10)
    def resume(self):
        self.client.get(self.trip_url.resume_url)
        self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.resume_data_url, params=self.trip_url.get_resume_params(),
                        name=self.trip_url.resume_data_url)

    @task(10)
    def map(self):
        self.client.get(self.trip_url.map_url)
        self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.map_data_url, params=self.trip_url.get_map_params(),
                        name=self.trip_url.map_data_url)

    @task(10)
    def large_trips(self):
        self.client.get(self.trip_url.large_trips_url)
        self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.large_trips_data_url, params=self.trip_url.get_large_trips_params(),
                        name=self.trip_url.large_trips_data_url)

    @task(10)
    def from_to_maps(self):
        self.client.get(self.trip_url.from_to_map_url)
        self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.from_to_map_data_url, params=self.trip_url.get_from_to_map_params(),
                        name=self.trip_url.from_to_map_data_url)

    @task(10)
    def strategies(self):
        self.client.get(self.trip_url.strategies_url)
        self.client.get(self.trip_url.available_days_url)
        self.client.get(self.trip_url.strategies_data_url, params=self.trip_url.get_strategies_params(),
                        name=self.trip_url.strategies_data_url)

    @task(50)
    def stop(self):
        self.interrupt()
