import json

import requests
from django.conf import settings
from django.http.response import HttpResponse
from django.utils.deprecation import MiddlewareMixin
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.exceptions import AuthenticationFailed


class EstiamAuthenticationMiddleware(MiddlewareMixin):
    keyword = "Estiam"
    auth_url = settings.AUTH_ESTIAM_SERVICE + "api/auth/me/"
    validate_token_url = settings.AUTH_ESTIAM_SERVICE + "api/auth/token/verify/"

    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        jwt_token = request.headers.get("authorization", None)
        if jwt_token is None:
            return HttpResponse(json.dumps({"detail": "missing token"}), status=401)
        else:
            jwt_token = request.headers.get("authorization", None).split()[1]

        if jwt_token:
            request = requests.post(
                url=self.validate_token_url, data={"token": jwt_token}
            )
            if not request.ok:
                return HttpResponse(
                    json.dumps(AuthenticationFailed(_("Invalid or expired token."))),
                    status=401,
                )
            response = requests.get(
                url=self.auth_url,
                headers={"Authorization": f"{self.keyword} {jwt_token}"},
            )
            if not response:
                msg = response.json()["detail"]
                return HttpResponse(json.dumps(msg), status=401)
        else:
            return HttpResponse(
                json.dumps({"detail": "missing token, pls provided a valid token"}),
                status=401,
            )
