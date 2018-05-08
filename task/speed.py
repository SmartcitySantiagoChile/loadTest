from locust import TaskSet, task

import urls


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
