from drf_spectacular.contrib.rest_framework_simplejwt import SimpleJWTScheme

from user_management_service.auth import EstiamAuthentication


class EstiamJWTokenUserScheme(SimpleJWTScheme):
    target_class = EstiamAuthentication
