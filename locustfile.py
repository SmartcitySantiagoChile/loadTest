# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from locust import HttpLocust, TaskSet, task

import urls
from bs4 import BeautifulSoup


class UserBehavior(TaskSet):

    def login(self):
        login_url = urls.Login()
        response = self.client.get(login_url.login_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        csrfmiddlewaretoken_value = soup.find('input', {'name': 'csrfmiddlewaretoken'}).get('value')
        params = login_url.login_parameters.copy()
        params['csrfmiddlewaretoken'] = csrfmiddlewaretoken_value

        self.client.post(login_url.login_url, params)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    @task(10)
    def expedition(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.expedition)
        self.client.get(profile_url.expedition_data_url, params=profile_url.expedition_data_params)

    @task(1)
    def stop(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.stop)

    @task(1)
    def trajectory(self):
        profile_url = urls.Profile()
        self.client.get(profile_url.trajectory)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000 * 5
    max_wait = 1000 * 10
