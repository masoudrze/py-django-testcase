from django.test import TestCase
from django.contrib.auth.models import User
# Create your tests here.
from django.test import SimpleTestCase


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