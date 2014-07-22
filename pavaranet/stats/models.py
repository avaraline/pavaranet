from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _

from pavaranet.social.models import Clan, Player

class AbstractBaseStats(models.Model):
    """
    An abstract base class that adds the fields, properties, and methods for
    every statistic we want to track.
    """
    # TODO: Think of more things to track. Seconds on hill? Flags captured? etc.
    points = models.IntegerField(_('points'), default=0, editable=False)
    kills = models.PositiveIntegerField(_('kills'), default=0, editable=False)
    deaths = models.PositiveIntegerField(_('deaths'), default=0, editable=False)
    boosters_used = models.PositiveIntegerField(_('boosters used'), default=0,
        editable=False)
    missiles_fired = models.PositiveIntegerField(_('missiles fired'), default=0,
        editable=False)
    missiles_damage = models.FloatField(_('missile damage dealt'), default=0.0,
        editable=False)
    missiles_accuracy = models.FloatField(_('missile accuracy'), default=0.0,
        editable=False)
    grenades_fired = models.PositiveIntegerField(_('grenades fired'), default=0,
        editable=False)
    grenades_damage = models.FloatField(_('grenade damage dealt'), default=0.0,
        editable=False)
    grenades_accuracy = models.FloatField(_('grenade accuracy'), default=0.0,
        editable=False)
    plasma_fired = models.PositiveIntegerField(_('plasma fired'), default=0,
        editable=False)
    plasma_damage = models.FloatField(_('plasma damage dealt'), default=0.0,
        editable=False)
    plasma_accuracy = models.FloatField(_('plasma accuracy'), default=0.0,
        editable=False)
    plasma_efficiency = models.FloatField(_('plasma efficiency'), default=0.0,
        editable=False)

    class Meta:
        abstract = True

    def get_kd_ratio(self):
        return self.kills / self.deaths if self.deaths else self.kills
    kd_ratio = property(get_kd_ratio)


class ClanAggregate(AbstractBaseStats):
    """
    Aggregated statistics for an entire clan's current membership.
    """
    clan = models.OneToOneField(Clan, related_name='stats', editable=False)
    skill_rating = models.PositiveSmallIntegerField(_('skill rating'),
        default=0, editable=False)

    def __str__(self):
        return 'Statistics for {0}'.format(self.clan.name)


class PlayerAggregate(AbstractBaseStats):
    """
    Aggregated statistics for a player's entire game history.
    """
    player = models.OneToOneField(Player, related_name='stats', editable=False)
    skill_rating = models.PositiveSmallIntegerField(_('skill rating'),
        default=0, editable=False)

    def __str__(self):
        return 'Statistics for {0}'.format(self.player.full_handle)

    def save(self, *args, **kwargs):
        super(PlayerAggregate, self).save(*args, **kwargs)
        # TODO: Develop an algorithm for calculating skill rating
        # TODO: If the player belongs to a clan, update the ClanAggregate


class GameSnapshot(models.Model):
    # TODO: Subclass AbstractBaseStats and aggregate participants' stats?
    # TODO: Replace or supplement map_name with a ForeignKey to the asset
    # TODO: Add game_type field?
    map_name = models.CharField(_('map name'), max_length=30, editable=False)
    date_started = models.DateTimeField(_('time started'), editable=False)
    date_ended = models.DateTimeField(_('time ended'), editable=False)

    def __str__(self):
        return '{0} on {1}'.format(self.map_name, self.date_started)

    def get_game_duration(self):
        return str(self.date_ended - self.date_started)
    game_duration = property(get_game_duration)


class PlayerSnapshot(AbstractBaseStats):
    # TODO: Include player loadout?
    game = models.ForeignKey(GameSnapshot, related_name='players',
        editable=False)
    player = models.ForeignKey(Player, related_name='games',
        editable=False)
    handle = models.CharField(_('handle'), editable=False,
        max_length=settings.PAVARANET_HANDLE_MAX_LENGTH + \
                    len(str(max(settings.PAVARANET_HANDLE_CODE_RANGE))) + 1)
    team = models.PositiveSmallIntegerField(_('team'), blank=True, null=True,
        editable=False)

    def __str__(self):
        return self.handle

    def save(self, *args, **kwargs):
        super(PlayerSnapshot, self).save(*args, **kwargs)
        # TODO: Update PlayerAggregate for this player
