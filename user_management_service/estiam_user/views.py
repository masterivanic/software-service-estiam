from estiam_user.models import EstiamUser
from estiam_user.serializers import UserSerializer
from rest_framework import viewsets


class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = EstiamUser.objects.all()
