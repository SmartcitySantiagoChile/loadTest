# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from bs4 import BeautifulSoup
from locust import HttpLocust, TaskSet, task

import urls


def login(l):
    login_url = urls.Login()
    response = l.client.get(login_url.login_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrfmiddlewaretoken_value = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
    params = login_url.login_parameters.copy()
    params['csrfmiddlewaretoken'] = csrfmiddlewaretoken_value

    l.client.post(login_url.login_url, params)


class ProfileUserBehavior(TaskSet):

    @task(60)
    def expedition(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.expedition_url)
        self.client.get(profile_url.expedition_data_url, params=profile_url.get_expedition_data_params(),
                        name=profile_url.expedition_data_url)

    @task(10)
    def bus_stop(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.stop_url)
        self.client.get(profile_url.stop_data_url, params=profile_url.get_stop_data_params(),
                        name=profile_url.stop_data_url)

    @task(10)
    def matrix(self):
        odbyroute_url = urls.ODByRoute()
        self.client.get(odbyroute_url.matrix_url)
        self.client.get(odbyroute_url.matrix_data_url, params=odbyroute_url.get_matrix_data_params(),
                        name=odbyroute_url.matrix_data_url)

    @task(5)
    def trajectory(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.trajectory_url)

    @task(5)
    def stop(self):
        self.interrupt()


class SpeedUserBehavior(TaskSet):

    @task(30)
    def matrix(self):
        speed_url = urls.Speed()
        self.client.get(speed_url.matrix_url)
        self.client.get(speed_url.matrix_data_url, params=speed_url.get_matrix_data_params(),
                        name=speed_url.matrix_data_url)

    @task(30)
    def ranking(self):
        speed_url = urls.Speed()
        self.client.get(speed_url.ranking_url)
        self.client.get(speed_url.ranking_data_url, params=speed_url.get_ranking_data_params(),
                        name=speed_url.ranking_data_url)

    @task(30)
    def trajectory(self):
        speed_url = urls.Speed()
        self.client.get(speed_url.variation_url)
        self.client.get(speed_url.variation_data_url, params=speed_url.get_variation_data_params(),
                        name=speed_url.variation_data_url)

    @task(10)
    def stop(self):
        self.interrupt()


class TripUserBehavior(TaskSet):

    @task
    def index(self):
        pass



class MasterUserBehavior(TaskSet):
    tasks = {
        ProfileUserBehavior: 60,
        SpeedUserBehavior: 20,
        TripUserBehavior: 20
    }

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        login(self)


class WebsiteUser(HttpLocust):
    task_set = MasterUserBehavior
    min_wait = 1000 * 5
    max_wait = 1000 * 10
