# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ClanAggregate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('points', models.IntegerField(default=0, editable=False, verbose_name='points')),
                ('kills', models.PositiveIntegerField(default=0, editable=False, verbose_name='kills')),
                ('deaths', models.PositiveIntegerField(default=0, editable=False, verbose_name='deaths')),
                ('missiles_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='missiles fired')),
                ('grenades_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='grenades fired')),
                ('plasma_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='plasma fired')),
                ('skill_rating', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='skill rating')),
                ('clan', models.OneToOneField(to='social.Clan', editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GameSnapshot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('map_name', models.CharField(editable=False, verbose_name='map name', max_length=30)),
                ('date_started', models.DateTimeField(editable=False, verbose_name='time started')),
                ('date_ended', models.DateTimeField(editable=False, verbose_name='time ended')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerAggregate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('points', models.IntegerField(default=0, editable=False, verbose_name='points')),
                ('kills', models.PositiveIntegerField(default=0, editable=False, verbose_name='kills')),
                ('deaths', models.PositiveIntegerField(default=0, editable=False, verbose_name='deaths')),
                ('missiles_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='missiles fired')),
                ('grenades_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='grenades fired')),
                ('plasma_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='plasma fired')),
                ('skill_rating', models.PositiveSmallIntegerField(default=0, editable=False, verbose_name='skill rating')),
                ('player', models.OneToOneField(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlayerSnapshot',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('points', models.IntegerField(default=0, editable=False, verbose_name='points')),
                ('kills', models.PositiveIntegerField(default=0, editable=False, verbose_name='kills')),
                ('deaths', models.PositiveIntegerField(default=0, editable=False, verbose_name='deaths')),
                ('missiles_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='missiles fired')),
                ('grenades_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='grenades fired')),
                ('plasma_fired', models.PositiveIntegerField(default=0, editable=False, verbose_name='plasma fired')),
                ('handle', models.CharField(editable=False, verbose_name='handle', max_length=25)),
                ('team', models.PositiveSmallIntegerField(blank=True, editable=False, null=True, verbose_name='team')),
                ('game', models.ForeignKey(to='stats.GameSnapshot', editable=False)),
                ('player', models.ForeignKey(to=settings.AUTH_USER_MODEL, editable=False)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
