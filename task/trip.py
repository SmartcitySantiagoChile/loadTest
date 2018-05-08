from locust import TaskSet, task


class TripUserBehavior(TaskSet):

    @task
    def index(self):
        pass
