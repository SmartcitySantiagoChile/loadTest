from locust import HttpLocust, TaskSet

from task.profile import ProfileUserBehavior
from task.speed import SpeedUserBehavior
from task.trip import TripUserBehavior
from url.utils import Login


def login(l):
    login_instance = Login()
    response = l.client.get(login_instance.login_url)
    csrf_token = response.cookies['csrftoken']

    headers = {
        'X-CSRFToken': csrf_token,
        'Referer': l.client.base_url
    }
    l.client.post(login_instance.login_url, login_instance.login_parameters, headers=headers)


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
