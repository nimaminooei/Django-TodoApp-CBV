from django.contrib.auth.models import User
from rest_framework.test import APIClient
from datetime import datetime
import pytest
from django.urls import reverse

@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        username="nimaa", password="Nima1234@", is_verified=True
    )
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("todo:api:task_list")
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401_status(self, api_client):
        url = reverse("todo:api:task_list")
        data = {
            "task": "test",
            "status": True,
            
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(self, api_client, common_user):
        url = reverse("todo:api:task_list")
        data = {
            "task": "test",
            "status": True,
            
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("todo:api:task_list")
        data = {
            "status": True,
            
        }
        user = common_user

        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400