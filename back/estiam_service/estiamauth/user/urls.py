from django.urls import path
from estiamauth.user.views import *
from rest_framework.routers import DefaultRouter


app_name = "administration"

router = DefaultRouter()
router.register("users", AdminUserViewSetViewSet, basename="users")

urlpatterns = [
    path("login/", AdminObtainTokenView.as_view(), name="token"),
]

urlpatterns += router.urls
