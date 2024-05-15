import json

import pytest
from django.urls import reverse
from estiamauth.authentication.views import EstiamAuthViewSet
from estiamauth.user.models import EstiamUser
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory
from rest_framework_simplejwt.tokens import RefreshToken


@pytest.mark.django_db
class TestAuthenticationAndAuthorization:
    api_client = APIClient()

    def test_user_login(self, build_user):
        user = build_user()
        url = reverse("token")
        data = {
            "email": user.email,
            "password": "testpassword",
        }

        response = self.api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
        assert "access" in json.loads(response.content)

    def test_user_registration(self):
        url = reverse("users-register")
        user_data = {
            "email": "abcdeff@example.com",
            "username": "abcdeff",
            "first_name": "Test",
            "last_name": "User",
            "password": "testpassword",
            "password2": "testpassword",
        }
        request = APIRequestFactory().post(url, user_data, format="json")
        response = EstiamAuthViewSet.as_view({"post": "register"})(request)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["email"] == user_data["email"]
        assert response.data["username"] == user_data["username"]
        assert EstiamUser.objects.get(email=user_data["email"]) != None

    def test_user_change_password(self, build_user):
        url = reverse("users-change-password")

        user_old_password = "mypassword"
        user_new_password = "mynew_password"

        user = build_user(password=user_old_password)

        passwords = {
            "old_password": user_old_password,
            "new_password": user_new_password,
            "confirm_password": user_new_password,
        }

        user_token = RefreshToken.for_user(user)
        self.api_client.credentials(
            HTTP_AUTHORIZATION=f"Estiam {user_token.access_token}"
        )
        response = self.api_client.post(url, passwords, format="json")
        assert response.status_code == status.HTTP_200_OK

    def test_user_profile(self, build_user):
        url = reverse("users-me")

        user = build_user()

        user_token = RefreshToken.for_user(user)
        self.api_client.credentials(
            HTTP_AUTHORIZATION=f"Estiam {user_token.access_token}"
        )
        self.api_client.force_authenticate(user=user)
        response = self.api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == user.email
        assert response.data["username"] == user.username
        assert response.data["first_name"] == user.first_name
        assert response.data["last_name"] == user.last_name

    def test_user_logout(self, build_user):
        url = reverse("users-logout")
        user = build_user(is_confirmed=True)
        refresh = RefreshToken.for_user(user)
        data = {"refresh": str(refresh)}
        self.api_client.credentials(HTTP_AUTHORIZATION=f"Estiam {refresh.access_token}")
        response = self.api_client.post(url, data, format="json")
        assert response.status_code == status.HTTP_200_OK
