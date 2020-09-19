from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = 'users'
    verbose_name = _("users")

    def ready(self):
        try:
            from . import signals  # noqa F401
        except ImportError as e:
            raise e
