from django.contrib.auth.models import User
from rest_framework.test import APIClient
import pytest
from django.urls import reverse


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def user_auth():
    user = User.objects.create_user(
        email="nimnim@nimnim.com", username="nimaa", password="Nima1234@"
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_tasks_response_200_status(self, api_client, user_auth):
        url = reverse("todo:api:task_list")
        user = user_auth
        api_client.force_authenticate(user=user)
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_tasks_response_401_status(self, api_client):
        url = reverse("todo:api:task_list")
        data = {
            "task": "test",
            "status": True,
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_tasks_response_201_status(self, api_client, user_auth):
        url = reverse("todo:api:task_list")
        data = {
            "task": "test",
            "status": True,
        }
        user = user_auth
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_tasks_invalid_data_response_400_status(
        self, api_client, user_auth
    ):
        url = reverse("todo:api:task_list")
        data = {
            "status": True,
        }
        user = user_auth

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400
