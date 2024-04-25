from django.apps import AppConfig


class EstiamUserConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "estiam_user"

    def ready(self):
        import user_management_service.schema
