import unittest

from src.gorest_handler import GorestAPIHandler


class TestGorest(unittest.TestCase):

    def setUp(self) -> None:
        self.gorest_handler = GorestAPIHandler(
            "Bearer 106f3e7a3a32bcf14303de2cbfa28452a0e1dd3880d2a11676bc11971f186ebb")

    def test_user_create(self):
        response_body, _ = self.gorest_handler.create_user()
        self.assertIn("id", response_body["data"])
        response_body, status_code = self.gorest_handler.get_user(response_body["data"]["id"])
        self.assertEqual(status_code, 200)

    def test_user_update(self):
        new_name = {"name": "Test Test"}
        response_body, _ = self.gorest_handler.create_user()
        response_body, status_code = self.gorest_handler.update_user(response_body["data"]["id"], new_name)
        self.assertEqual(status_code, 200)
        self.assertEqual(response_body["data"]["name"], new_name["name"])

    def test_user_delete(self):
        response_body, _ = self.gorest_handler.create_user()
        status_code = self.gorest_handler.delete_user(response_body["data"]["id"])
        self.assertEqual(status_code, 204)
