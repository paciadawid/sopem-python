import unittest
import time
from faker import Faker
import requests
from src.gorest_handler import GorestAPIHandler

class TestGorest(unittest.TestCase):

    def setUp(self) -> None:
        self.gorest_handler = GorestAPIHandler("Bearer 106f3e7a3a32bcf14303de2cbfa28452a0e1dd3880d2a11676bc11971f186ebb")

    def test_user_create(self):
        response_body, status_code = self.gorest_handler.create_user()
        self.assertIn("id", response_body["data"])
        response_body, status_code = self.gorest_handler.get_user(response_body["data"]["id"])
        self.assertEqual(status_code, 200)
