from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from django.test import SimpleTestCase
from .validators import validate_password


# class LoginTests(SimpleTestCase):
#     def test_valid_credentials(self):
#         response = self.client.post(
#             "/api/login/",
#             {
#                 "username": "admin",
#                 "password": "123456"
#             }
#         )

#         self.assertEqual(response.status_code, 200)


#     def test_invalid_credentials(self):
#         response = self.client.post(
#             "/api/login/",
#             {
#                 "username": "admin",
#                 "password": "000000"
#             }
#         )

#         self.assertEqual(response.status_code, 401)


#     def test_empty_credentials(self):
#         response = self.client.post(
#             "/api/login/",
#             {}
#         )

#         self.assertEqual(response.status_code, 401)


class LoginTests(TestCase):

    def setUp(self):
        User.objects.create_user(
            username="admin",
            password="123456"
        )

    def test_valid_credentials(self):
        response = self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"123456"
            }
        )

        self.assertEqual(response.status_code, 200)


    def test_invalid_credentials(self):
        response = self.client.post(
            "/api/login/",
            {
                "username":"admin",
                "password":"000000"
            }
        )

        self.assertEqual(response.status_code, 401)


    def test_empty_credentials(self):
        response = self.client.post(
            "/api/login/",
            {}
        )

        self.assertEqual(response.status_code, 401)

class PasswordTests(SimpleTestCase):

    def test_valid_password(self):
        self.assertTrue(validate_password("123456789"))

    def test_short_password(self):
        self.assertFalse(validate_password("123"))

    def test_empty_password(self):
        self.assertFalse(validate_password(""))

    def test_boundry_password(self):
        self.assertTrue(validate_password("12345678"))

    def test_below_boundry_password(self):
        self.assertFalse(validate_password("1234567"))

    def test_none_password(self):
        self.assertFalse(validate_password(None))