import unittest
import time
from faker import Faker
import requests


class TestGorest(unittest.TestCase):

    def setUp(self) -> None:
        self.token = {
            "Authorization": "Bearer 106f3e7a3a32bcf14303de2cbfa28452a0e1dd3880d2a11676bc11971f186ebb"
        }
        self.fake = Faker()
        self.base_url = "https://gorest.co.in/public/v1"
        self.user_url = "/users"

    def test_user_create(self):
        user = {
            "name": self.fake.name(),
            "gender": "male",
            "email": self.fake.email(),
            "status": "active"
        }

        response_body = requests.post(f"{self.base_url}{self.user_url}", data=user, headers=self.token).json()
        self.assertIn("id", response_body["data"])
        id = response_body["data"]["id"]
        res2 = requests.get(f"{self.base_url}{self.user_url}/{id}", headers=self.token)

        self.assertEqual(res2.status_code, 200)
        self.assertDictContainsSubset(user, res2.json()["data"])