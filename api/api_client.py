import requests

class APIClient:
    BASE_URL = "https://reqres.in/api"

    def get_users(self):
        return requests.get(f"{self.BASE_URL}/users")

    def create_user(self, data):
        return requests.post(f"{self.BASE_URL}/users", json=data)
