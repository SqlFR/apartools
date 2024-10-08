from django.apps import AppConfig


class IssuesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'issues'
    verbose_name = 'Les incidents'

    def ready(self):
        import issues.signals
