from django.contrib.auth import get_user_model
from estiamauth.authentication.serializers import ObtainTokenSerializer
from estiamauth.authentication.serializers import PasswordResetConfirmSerializer
from estiamauth.authentication.serializers import UserChangePasswordSerializer
from estiamauth.authentication.serializers import UserProfileSerializer
from estiamauth.authentication.serializers import UserRegistrationSerializer
from estiamauth.authentication.serializers import UserSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.serializers import TokenBlacklistSerializer
from rest_framework_simplejwt.views import TokenBlacklistView
from rest_framework_simplejwt.views import TokenObtainPairView


class ObtainTokenView(TokenObtainPairView):
    serializer_class = ObtainTokenSerializer


class EstiamAuthViewSet(viewsets.GenericViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        action = self.action
        match action:
            case "register":
                return UserRegistrationSerializer
            case "change_password":
                return UserChangePasswordSerializer
            case "reset_password":
                return PasswordResetConfirmSerializer
            case "me":
                return UserProfileSerializer
            case "logout":
                return TokenBlacklistSerializer
            case _:
                return self.serializer_class

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(AllowAny,),
    )
    def register(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "username": user.username,
                "email": user.email,
                "message": "Registration Successful. ",
            },
            status=status.HTTP_201_CREATED,
        )

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(IsAuthenticated,),
        url_path="password/change",
    )
    def change_password(self, request: Request) -> Response:
        serializer = self.get_serializer(
            data=request.data, context={"user": request.user}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Password Changed Successfully"}, status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=["POST"],
        permission_classes=(AllowAny,),
        url_path="password/reset",
    )
    def reset_password(self, request: Request) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Password Reset Successfully"}, status=status.HTTP_200_OK
        )

    @action(
        detail=False,
        methods=("GET",),
        authentication_classes=(JWTAuthentication,),
        permission_classes=(IsAuthenticated,),
    )
    def me(self, request: Request) -> Response:
        serializer = self.get_serializer(instance=request.user)
        return Response(serializer.data)

    @action(detail=False, methods=("POST",), permission_classes=(IsAuthenticated,))
    def logout(self, request: Request) -> Response:
        logout_view = TokenBlacklistView.as_view()
        response = logout_view(request._request)
        return response
