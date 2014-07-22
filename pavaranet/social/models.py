import random
import re

from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
    PermissionsMixin)
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import (MinValueValidator, MaxValueValidator,
    RegexValidator)
from django.db import models
from django.utils.translation import ugettext_lazy as _


CLAN_RANKS = (
    (1, _('Leader')),
    (2, _('Officer')),
    (3, _('Member')),
)

# TODO: Blacklist certain patterns via settings.PAVARANET_NAMING_BANNED_WORDS
VALID_NAME = [RegexValidator(
    regex=settings.PAVARANET_NAMING_REGEX,
    message=_(settings.PAVARANET_NAMING_ERROR),
    flags=re.I
)]

VALID_HANDLE_CODE = [
    MinValueValidator(min(settings.PAVARANET_HANDLE_CODE_RANGE)),
    MaxValueValidator(max(settings.PAVARANET_HANDLE_CODE_RANGE)),
]


def _default_handle_code():
    return random.choice(settings.PAVARANET_HANDLE_CODE_RANGE)


class Clan(models.Model):
    name = models.CharField(_('name'), unique=True, validators=VALID_NAME,
        max_length=settings.PAVARANET_CLAN_NAME_MAX_LENGTH)
    tag = models.CharField(_('tag'), unique=True,
        max_length=settings.PAVARANET_CLAN_TAG_MAX_LENGTH)
    information = models.CharField(_('information'), blank=True,
        max_length=1500)
    message = models.CharField(_('message of the day'), blank=True,
        max_length=250)
    is_recruiting = models.BooleanField(_('recruiting'), db_index=True,
        default=True)
    date_founded = models.DateTimeField(_('date founded'), editable=False,
        auto_now_add=True)

    def __str__(self):
        return '{0} <{1}>'.format(self.name, self.tag)


class PlayerManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password=None,
                    **extra_fields):
        """
        Creates and saves a User with the given email, first name, last name,
        and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        if not first_name:
            raise ValueError('Users must have a first name')
        if not last_name:
            raise ValueError('Users must have a last name')

        user = self.model(
            email=email.strip().lower(),
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password,
                         **extra_fields):
        """
        Creates and saves a superuser with the given email, first name, last
        name, and password.
        """
        extra_fields.pop('is_staff', True)
        extra_fields.pop('is_superuser', True)
        return self.create_user(
            email,
            first_name,
            last_name,
            password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )


class Player(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True, max_length=254)
    handle = models.CharField(_('handle'), validators=VALID_NAME,
        max_length=settings.PAVARANET_HANDLE_MAX_LENGTH)
    handle_code = models.PositiveSmallIntegerField(_('handle code'),
        default=_default_handle_code, validators=VALID_HANDLE_CODE,
        editable=False,
        help_text=_('Randomized identifier that allows multiple players to use '
                    'the same handle. Used in friend requests and such.'))
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    clan = models.ForeignKey(Clan, related_name='members', blank=True,
        null=True, editable=False)
    clan_rank = models.PositiveSmallIntegerField(_('clan rank'), editable=False,
        choices=CLAN_RANKS, default=3)
    is_active = models.BooleanField(_('active status'), db_index=True,
        default=True,
        help_text=_('Designates whether this player can currently login. '
                    'Uncheck this instead of deleting accounts.'))
    is_developer = models.BooleanField(_('developer status'), default=False,
        help_text=_('Designates whether this player was involved in pavara\'s '
                    'development.'))
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether this user can administer the website.'))
    date_joined = models.DateTimeField(_('date joined'), editable=False,
        auto_now_add=True)

    objects = PlayerManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'handle', 'handle_code']

    class Meta:
        unique_together = (('handle', 'handle_code'),)

    def __init__(self, *args, **kwargs):
        super(Player, self).__init__(*args, **kwargs)
        self._initial_handle = self.handle
        self._initial_handle_code = self.handle_code

    def __str__(self):
        return self.full_handle

    def clean(self):
        # Check to see if either of the player's handle fields have changed. If
        # they have, a new value for handle_code may be necessary.
        handle_changed = (self.handle != self._initial_handle)
        handle_code_changed = (self.handle_code != self._initial_handle_code)
        if handle_changed or handle_code_changed or not self.pk:
            players_with_handle = Player.objects.filter(handle=self.handle)
            reserved = {p.handle_code for p in players_with_handle}
            remaining = set(settings.PAVARANET_HANDLE_CODE_RANGE) - reserved
            if not remaining:
                raise ValidationError(
                    _('"%(handle)s" is currently in use by too many players.'),
                    code='unavailable',
                    params={'handle': self.handle}
                )
            if self.handle_code not in remaining:
                self.handle_code = random.sample(remaining, 1)[0]

    def save(self, *args, **kwargs):
        super(Player, self).save(*args, **kwargs)
        self._initial_handle = self.handle
        self._initial_handle_code = self.handle_code

    def email_user(self, subject, message, from_email=None, **kwargs):
        """
        Sends an email to this player.
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def get_full_name(self):
        """
        Returns the player's first and last name, with a space in between.
        """
        return '{0} {1}'.format(self.first_name, self.last_name)
    full_name = property(get_full_name)

    def get_short_name(self):
        """
        Returns the player's first name.
        """
        return self.first_name
    short_name = property(get_short_name)

    def get_full_handle(self):
        """
        Returns the player's full, unique handle.
        """
        if self.handle and self.handle_code:
            return '{0}#{1}'.format(self.handle, self.handle_code)
        else:
            return ''
    full_handle = property(get_full_handle)


class AbstractBaseInvite(models.Model):
    sender = models.ForeignKey(Player, related_name='%(class)ss_sent',
        editable=False)
    receiver = models.ForeignKey(Player, related_name='%(class)ss_received',
        editable=False)
    date_sent = models.DateTimeField(_('date sent'), editable=False,
        auto_now_add=True)

    class Meta:
        abstract = True


class ClanInvite(AbstractBaseInvite):
    clan = models.ForeignKey(Clan, related_name='invites', editable=False)

    def __str__(self):
        return '{0} invited {1} to {2}'.format(
            self.sender.full_handle,
            self.receiver.full_handle,
            self.clan.name,
        )


class FriendInvite(AbstractBaseInvite):

    def __str__(self):
        return '{0} invited {1} to be friends'.format(
            self.sender.full_handle,
            self.receiver.full_handle,
        )


class RealNameInvite(AbstractBaseInvite):

    def __str__(self):
        return '{0} invited {1} to exchange their real names'.format(
            self.sender.full_handle,
            self.receiver.full_handle,
        )
