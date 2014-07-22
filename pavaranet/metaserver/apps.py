from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MetaServerConfig(AppConfig):
    name = 'pavaranet.metaserver'
    verbose_name = _('pavaranet metaserver')
