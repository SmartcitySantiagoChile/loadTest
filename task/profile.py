from locust import TaskSet, task

import urls


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

    @task(10)
    def transfer(self):
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
