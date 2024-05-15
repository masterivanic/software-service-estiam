from django.urls import include
from django.urls import path
from estiam_user.views import UserViewset
from rest_framework.routers import DefaultRouter

app_name = "user management"

router = DefaultRouter()
router.register("users", UserViewset, basename="users")

urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += router.urls
