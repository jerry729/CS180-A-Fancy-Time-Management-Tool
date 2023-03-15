import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scheduler.settings')

import django
import json
django.setup()
import pytest
import random
import string
from http import HTTPStatus
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from app_calendar.models import UserInfo, TaskInfo
from .serializer import UserSerializer, TaskSerializer


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def test_user():
    user = UserInfo.objects.create(
        user_name="test_user",
        password="test_password"
    )
    return user

def random_string(length):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@pytest.mark.django_db
def test_user_login_random_inputs(api_client, test_user):
    url = reverse("user-login")

    for _ in range(100):
        random_user_name = random_string(10)
        random_password = random_string(10)

        # Create a random user
        random_user = UserInfo.objects.create(
            user_name=random_user_name,
            password=random_password
        )

        # Test successful login with the correct credentials
        response = api_client.get(url, {"user_name": random_user.user_name, "password": random_user.password})
        assert response.status_code == 200
        assert len(response.json()) == 1
        assert response.json()[0]["user_name"] == random_user.user_name
        assert response.json()[0]["password"] == random_user.password

        # Test unsuccessful login with incorrect password
        response = api_client.get(url, {"user_name": random_user.user_name, "password": "wrong_password"})
        assert response.status_code == 200
        assert len(response.json()) == 0

        # Clean up the created user
        random_user.delete()