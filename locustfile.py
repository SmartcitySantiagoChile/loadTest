from locust import HttpLocust, TaskSet

from task.profile import ProfileUserBehavior
from task.speed import SpeedUserBehavior
from task.trip import TripUserBehavior
from url.utils import Login


class MasterUserBehavior(TaskSet):
    tasks = {
        ProfileUserBehavior: 60,
        SpeedUserBehavior: 20,
        TripUserBehavior: 20
    }

    def login(self):
        login_instance = Login()
        response = self.client.get(login_instance.login_url)
        csrf_token = response.cookies['csrftoken']

        headers = {
            'X-CSRFToken': csrf_token,
            'Referer': self.client.base_url
        }
        self.client.post(login_instance.login_url, login_instance.login_parameters, headers=headers)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()


class WebsiteUser(HttpLocust):
    task_set = MasterUserBehavior
    min_wait = 1000 * 30
    max_wait = 1000 * 60
