from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class StudyCenterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'study_center'
    verbose_name = _('Study center')
