from django.apps import AppConfig


class AccessoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accessories'
    verbose_name = 'Les accessoires'

    def ready(self):
        import accessories.signals
