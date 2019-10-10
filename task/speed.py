from locust import TaskSet, task

from url.speed import Speed


class SpeedUserBehavior(TaskSet):

    def __init__(self, parent):
        super(SpeedUserBehavior, self).__init__(parent)
        self.speed_url = Speed()
        self.only_data = False

    @task(30)
    def matrix(self):
        if not self.only_data:
            self.client.get(self.speed_url.matrix_url)
            self.client.get(self.speed_url.available_days_url)
            self.client.get(self.speed_url.available_routes_url)
        self.client.get(self.speed_url.matrix_data_url, params=self.speed_url.get_matrix_data_params(),
                        name=self.speed_url.matrix_data_url)

    @task(30)
    def ranking(self):
        if not self.only_data:
            self.client.get(self.speed_url.ranking_url)
            self.client.get(self.speed_url.available_days_url)
            self.client.get(self.speed_url.available_routes_url)
        self.client.get(self.speed_url.ranking_data_url, params=self.speed_url.get_ranking_data_params(),
                        name=self.speed_url.ranking_data_url)

    @task(30)
    def trajectory(self):
        if not self.only_data:
            self.client.get(self.speed_url.variation_url)
            self.client.get(self.speed_url.available_days_url)
            self.client.get(self.speed_url.available_routes_url)
        self.client.get(self.speed_url.variation_data_url, params=self.speed_url.get_variation_data_params(),
                        name=self.speed_url.variation_data_url)

    @task(10)
    def stop(self):
        self.interrupt()
