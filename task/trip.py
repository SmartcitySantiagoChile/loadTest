# -*- coding: utf-8 -*-
from locust import TaskSet, task

from url.trip import Trip


class TripUserBehavior(TaskSet):

    def __init__(self, parent):
        super(TripUserBehavior, self).__init__(parent)
        self.speed_url = Trip()

    @task
    def index(self):
        pass
