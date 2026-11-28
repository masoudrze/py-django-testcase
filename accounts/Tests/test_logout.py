import allure
from unittest.mock import patch
from django.test import TestCase
from django.test import SimpleTestCase
from ..validators import validate_password
from django.contrib.auth.models import User