import factory
from estiamauth.models import EstiamUser


class UserModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = EstiamUser

    username = factory.Faker("user_name")
    email = factory.LazyAttribute(lambda obj: "%s@example.com" % obj.username)
    first_name = factory.Faker("name")
    last_name = factory.Faker("name")
    password = factory.django.Password("testpassword")
