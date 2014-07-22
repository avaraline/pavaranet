from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class AssetServerConfig(AppConfig):
    name = 'pavaranet.assetserver'
    verbose_name = _('pavaranet asset server')
