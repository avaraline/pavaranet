from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class StatsConfig(AppConfig):
    name = 'pavaranet.stats'
    verbose_name = _('pavaranet statistics module')
