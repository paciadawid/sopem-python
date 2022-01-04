import requests
from faker import Faker


class GorestAPIHandler:
    base_url = "https://gorest.co.in/public/v1"
    user_url = "/users"

    def __init__(self, token):
        self.token = {"Authorization": token}
        self.fake = Faker()

    def create_user(self):
        user = {
            "name": self.fake.name(),
            "gender": "male",
            "email": self.fake.email(),
            "status": "active"
        }
        res = requests.post(f"{self.base_url}{self.user_url}", data=user, headers=self.token)
        return res.json(), res.status_code

    def get_user(self, user_id):
        res = requests.get(f"{self.base_url}{self.user_url}/{user_id}", headers=self.token)
        return res.json(), res.status_code

    def update_user(self, user_id, new_data):
        res = requests.put(f"{self.base_url}{self.user_url}/{user_id}", data=new_data, headers=self.token)
        return res.json(), res.status_code

    def delete_user(self, user_id):
        res = requests.delete(f"{self.base_url}{self.user_url}/{user_id}", headers=self.token)
        return res.status_code
