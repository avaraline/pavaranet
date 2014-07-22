# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import pavaranet.social.models
import django.core.validators
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(help_text='Designates that this user has all permissions without explicitly assigning them.', default=False, verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('handle', models.CharField(validators=[django.core.validators.RegexValidator(flags=2, regex='^[A-Z][A-Z0-9\\ ]{2,}$', message='Names and handles must consist of letters, numbers, and spaces, begin with a letter, and be at least 3 characters long.')], max_length=20, verbose_name='handle')),
                ('handle_code', models.PositiveSmallIntegerField(help_text='Randomized identifier that allows multiple players to use the same handle. Used in friend requests and such.', default=pavaranet.social.models._default_handle_code, editable=False, validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(1999)], verbose_name='handle code')),
                ('first_name', models.CharField(verbose_name='first name', max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', max_length=30)),
                ('clan_rank', models.PositiveSmallIntegerField(default=3, editable=False, verbose_name='clan rank', choices=[(1, 'Leader'), (2, 'Officer'), (3, 'Member')])),
                ('is_active', models.BooleanField(help_text='Designates whether this player can currently login. Uncheck this instead of deleting accounts.', default=True, verbose_name='active status', db_index=True)),
                ('is_developer', models.BooleanField(help_text="Designates whether this player was involved in pavara's development.", default=False, verbose_name='developer status')),
                ('is_staff', models.BooleanField(help_text='Designates whether this user can administer the website.', default=False, verbose_name='staff status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Clan',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='name', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(flags=2, regex='^[A-Z][A-Z0-9\\ ]{2,}$', message='Names and handles must consist of letters, numbers, and spaces, begin with a letter, and be at least 3 characters long.')])),
                ('tag', models.CharField(max_length=6, unique=True, verbose_name='tag')),
                ('information', models.CharField(blank=True, verbose_name='information', max_length=1500)),
                ('message', models.CharField(blank=True, verbose_name='message of the day', max_length=250)),
                ('is_recruiting', models.BooleanField(default=True, verbose_name='recruiting', db_index=True)),
                ('date_founded', models.DateTimeField(auto_now_add=True, verbose_name='date founded')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='player',
            name='clan',
            field=models.ForeignKey(blank=True, to='social.Clan', editable=False, null=True),
            preserve_default=True,
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together=set([('handle', 'handle_code')]),
        ),
        migrations.CreateModel(
            name='ClanInvite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('clan', models.ForeignKey(to='social.Clan', editable=False)),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FriendInvite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RealNameInvite',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date_sent', models.DateTimeField(auto_now_add=True, verbose_name='date sent')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
                ('sender', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
