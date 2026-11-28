import allure
from unittest.mock import patch
from django.test import TestCase
from django.test import SimpleTestCase
from ..validators import validate_password
from django.contrib.auth.models import User


@allure.epic("Account Management")
@allure.feature("Authentication")
@allure.tag("Integration", "API")
class LoginTests(TestCase):

    def setUp(self):
        with allure.step("Create test user"):
            User.objects.create_user(
                username="admin",
                password="123456"
            )


    @allure.story("Valid Login")
    @allure.title("TC-LOGIN-001 | Valid credentials")
    @allure.description("Verify that a user can log in with valid credentials.")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_valid_credentials(self):

        allure.dynamic.parameter("Username", "admin")
        allure.dynamic.parameter("Password", "******")

        with allure.step("Send login request"):
            response = self.client.post(
                "/api/login/",
                {
                    "username":"admin",
                    "password":"123456"
                }
            )


        with allure.step("Attach API response"):
            allure.attach(
                response.content.decode("utf-8"),
                name="Response Body",
                attachment_type=allure.attachment_type.JSON
            )

            allure.attach(
                str(response.status_code),
                name="Status Code",
                attachment_type=allure.attachment_type.TEXT
            )

        with allure.step("Verify expected status code: 200"):
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