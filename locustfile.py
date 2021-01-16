from locust import HttpUser, task, between

class DdosUser(HttpUser):
    wait_time = between(1, 1)

    @task
    def ping(self):
        self.client.get('/')