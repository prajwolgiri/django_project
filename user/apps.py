from django.apps import AppConfig
# from .models import Profile


class UserConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'

    def ready(self):
        import user.signals
