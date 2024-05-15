from estiamauth.models import EstiamUser
from rest_framework import permissions


def user_authentication_rule(user: EstiamUser) -> bool:
    return user is not None
