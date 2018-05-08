# -*- coding: utf-8 -*-
from locust import TaskSet, task

from url.odbyroute import ODByRoute
from url.profile import Profile
from url.trip import Trip


class ProfileUserBehavior(TaskSet):

    def __init__(self, parent):
        super(ProfileUserBehavior, self).__init__(parent)
        self.profile_url = Profile()
        self.only_data = True

    @task(60)
    def expedition(self):
        if not self.only_data:
            self.client.get(self.profile_url.expedition_url)
            self.client.get(self.profile_url.available_days_url)
            self.client.get(self.profile_url.available_routes_url)
        self.client.get(self.profile_url.expedition_data_url, params=self.profile_url.get_expedition_data_params(),
                        name=self.profile_url.expedition_data_url)

    @task(10)
    def bus_stop(self):
        if not self.only_data:
            self.client.get(self.profile_url.stop_url)
            self.client.get(self.profile_url.available_days_url)
            self.client.get(self.profile_url.available_routes_url)
        self.client.get(self.profile_url.stop_data_url, params=self.profile_url.get_stop_data_params(),
                        name=self.profile_url.stop_data_url)

    @task(10)
    def matrix(self):
        odbyroute_url = ODByRoute()
        if not self.only_data:
            self.client.get(odbyroute_url.matrix_url)
            self.client.get(odbyroute_url.available_days_url)
            self.client.get(odbyroute_url.available_routes_url)
        self.client.get(odbyroute_url.matrix_data_url, params=odbyroute_url.get_matrix_data_params(),
                        name=odbyroute_url.matrix_data_url)

    @task(10)
    def transfer(self):
        trip_url = Trip()
        if not self.only_data:
            self.client.get(trip_url.transfer_url)
            self.client.get(trip_url.available_days_url)
        self.client.get(trip_url.transfer_data_url, params=trip_url.get_transfer_data_params(),
                        name=trip_url.transfer_data_url)

    @task(5)
    def trajectory(self):
        if not self.only_data:
            self.client.get(self.profile_url.trajectory_url)
            self.client.get(self.profile_url.available_days_url)
            self.client.get(self.profile_url.available_routes_url)
        self.client.get(self.profile_url.trajectory_data_url, params=self.profile_url.get_trajectory_data_params(),
                        name=self.profile_url.trajectory_data_url)

    @task(5)
    def stop(self):
        self.interrupt()
