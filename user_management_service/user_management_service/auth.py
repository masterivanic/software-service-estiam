import requests
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import AuthenticationFailed


class UserAuth(object):
    is_authenticated = True

    def __init__(self, any_dict) -> None:
        for key in any_dict:
            setattr(self, key, any_dict[key])


class EstiamAuthentication(JWTAuthentication):
    auth_url = settings.AUTH_ESTIAM_SERVICE + "api/auth/me/"
    validate_token_url = settings.AUTH_ESTIAM_SERVICE + "api/auth/token/verify/"

    keyword = "Estiam"

    def get_validated_token(self, raw_token):
        return raw_token.decode()

    def get_user(self, token):
        request = requests.post(url=self.validate_token_url, data={"token": token})
        if not request.ok:
            raise AuthenticationFailed(_("Invalid or expired token."))

        response = requests.get(
            url=self.auth_url, headers={"Authorization": f"{self.keyword} {token}"}
        )
        if not response:
            msg = response.json()["detail"]
            raise AuthenticationFailed(_(msg))
        else:
            response = response.json()
            user = UserAuth(response)
            return (user, token)
