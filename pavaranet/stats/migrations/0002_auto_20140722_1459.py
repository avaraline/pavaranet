# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanaggregate',
            name='boosters_used',
            field=models.PositiveIntegerField(verbose_name='boosters used', editable=False, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='boosters_used',
            field=models.PositiveIntegerField(verbose_name='boosters used', editable=False, default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='boosters_used',
            field=models.PositiveIntegerField(verbose_name='boosters used', editable=False, default=0),
            preserve_default=True,
        ),
    ]
