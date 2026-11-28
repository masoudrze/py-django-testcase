import allure
from unittest.mock import patch
from django.test import TestCase
from django.test import SimpleTestCase
from ..validators import validate_password
from django.contrib.auth.models import User


class SessionTests(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="admin",
            password="123456"
        )

    def test_valid_login_session(self):
        response = self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"123456"
            }
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn("_auth_user_id", self.client.session)

    def test_invalid_login_session(self):
        response = self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"000000"
            }
        )

        self.assertEqual(response.status_code, 401)
        self.assertNotIn("_auth_user_id", self.client.session)


    def test_session_user_id(self):
        response = self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"123456"
            }
        )

        self.assertEqual(
            self.client.session["_auth_user_id"],
            str(self.user.id)
        )

    def test_logout_session(self):
        self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"123456"
            }
        )

        self.assertIn("_auth_user_id", self.client.session)

        response = self.client.post("/api/logout/")

        self.assertEqual(response.status_code, 200)

        self.assertNotIn("_auth_user_id",self.client.session)