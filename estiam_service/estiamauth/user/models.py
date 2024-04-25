from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    ADMIN = "admin", "Administrateur"
    BLOGGER = "bloggeur", "Bloggeur"  # utilisateur final


class UserModel(AbstractUser):
    username = models.CharField(
        max_length=150,
        validators=[ASCIIUsernameValidator()],
        help_text=_(
            "Required. 150 characters or fewer. Lowercase a-z "
            "and uppercase A-Z letters, numbers"
        ),
        null=True,
    )
    email = models.EmailField(unique=True)
    confirm_number = models.CharField(max_length=1000, null=True)
    is_confirmed = models.BooleanField(default=True)
    roles = models.CharField(
        max_length=50, choices=UserRole.choices, default=UserRole.BLOGGER
    )
    created_by = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="created_by_user",
        null=True,
        blank=True,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=[
                    "confirm_number",
                ],
                name="confirm_number_unique",
            ),
        ]
        verbose_name = "User"

    def __str__(self):
        return (
            self.email + " (" + ("not " if not self.is_confirmed else "") + "confirmed)"
        )


class EstiamUser(UserModel):
    pass
