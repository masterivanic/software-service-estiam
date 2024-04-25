from estiam_user.models import EstiamUser
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = EstiamUser
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "roles",
        ]
