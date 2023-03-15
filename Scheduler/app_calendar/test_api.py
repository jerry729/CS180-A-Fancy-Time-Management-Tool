import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scheduler.settings')

import django
django.setup()

import json
import pytest
import random
import string
from http import HTTPStatus
from django.utils import timezone
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from app_calendar.models import UserInfo, TaskInfo
from .serializer import UserSerializer, TaskSerializer
from datetime import datetime, timedelta


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

    for _ in range(500):
        random_user_name = random_string(30)
        random_password = random_string(30)

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

@pytest.fixture
def create_random_task(test_user):
    def _create_random_task():
        task_name = ''.join(random.choices(string.ascii_letters, k=10))
        task_description = ''.join(random.choices(string.ascii_letters, k=20))
        start_time = timezone.now() + timedelta(days=random.randint(-30, 30))
        end_time = start_time + timedelta(hours=random.randint(1, 24))

        task = TaskInfo.objects.create(
            Task_owner_user=test_user.id,
            Task_name=task_name,
            Task_description=task_description,
            Task_start_time=start_time,
            Task_end_time=end_time
        )
        return task

    return _create_random_task

@pytest.mark.django_db
def test_get_tasks(api_client, test_user, create_random_task):
    tasks = [create_random_task() for _ in range(100)]

    url = reverse("get-tasks")
    response = api_client.get(url, {"user_id": test_user.id})
    assert response.status_code == 200
    assert len(response.json()) == 100

    task_ids = [task["id"] for task in response.json()]
    for task in tasks:
        assert task.id in task_ids