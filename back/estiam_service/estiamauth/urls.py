from django.urls import include
from django.urls import path
from estiamauth.authentication.views import EstiamAuthViewSet
from estiamauth.authentication.views import ObtainTokenView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

router = DefaultRouter()
router.register("", EstiamAuthViewSet, basename="users")

urlpatterns = [
    path("login/", ObtainTokenView.as_view(), name="token"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("", include(router.urls)),
]
