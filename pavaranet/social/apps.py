from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class SocialConfig(AppConfig):
    name = 'pavaranet.social'
    verbose_name = _('pavaranet social module')
