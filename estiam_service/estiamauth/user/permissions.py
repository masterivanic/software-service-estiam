from estiamauth.models import EstiamUser
from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class IsAdminOrBlogger(permissions.BasePermission):
    message = "user role not exist in system, pls contact the administrator"

    def has_permission(self, request: Request, view: ModelViewSet) -> bool:
        return request.user.roles in ["admin", "bloggeur"]


def user_admin_authentication_rule(user: EstiamUser) -> bool:
    return (
        user is not None and user.is_confirmed and user.roles in ["admin", "bloggeur"]
    )
