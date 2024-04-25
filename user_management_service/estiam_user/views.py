from estiam_user.models import EstiamUser
from estiam_user.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class UserViewset(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = EstiamUser.objects.all()
