import os
import sys

from locust import HttpLocust, TaskSet

sys.path.append(os.getcwd())

from task.profile import ProfileUserBehavior
from task.speed import SpeedUserBehavior
from task.trip import TripUserBehavior

from url.utils import Login


def login(l):
    login_url = Login()
    response = l.client.get(login_url.login_url)
    csrftoken = response.cookies['csrftoken']

    headers = {
        'X-CSRFToken': csrftoken
    }
    l.client.post(login_url.login_url, login_url.login_parameters, headers=headers)


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
    min_wait = 1000 * 30
    max_wait = 1000 * 60
