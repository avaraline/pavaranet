# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0002_auto_20140722_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='clanaggregate',
            name='grenades_accuracy',
            field=models.FloatField(default=0.0, verbose_name='grenade accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='grenades_damage',
            field=models.FloatField(default=0.0, verbose_name='grenade damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='missiles_accuracy',
            field=models.FloatField(default=0.0, verbose_name='missile accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='missiles_damage',
            field=models.FloatField(default=0.0, verbose_name='missile damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='plasma_accuracy',
            field=models.FloatField(default=0.0, verbose_name='plasma accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='plasma_damage',
            field=models.FloatField(default=0.0, verbose_name='plasma damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='clanaggregate',
            name='plasma_efficiency',
            field=models.FloatField(default=0.0, verbose_name='plasma efficiency', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='grenades_accuracy',
            field=models.FloatField(default=0.0, verbose_name='grenade accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='grenades_damage',
            field=models.FloatField(default=0.0, verbose_name='grenade damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='missiles_accuracy',
            field=models.FloatField(default=0.0, verbose_name='missile accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='missiles_damage',
            field=models.FloatField(default=0.0, verbose_name='missile damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='plasma_accuracy',
            field=models.FloatField(default=0.0, verbose_name='plasma accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='plasma_damage',
            field=models.FloatField(default=0.0, verbose_name='plasma damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playeraggregate',
            name='plasma_efficiency',
            field=models.FloatField(default=0.0, verbose_name='plasma efficiency', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='grenades_accuracy',
            field=models.FloatField(default=0.0, verbose_name='grenade accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='grenades_damage',
            field=models.FloatField(default=0.0, verbose_name='grenade damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='missiles_accuracy',
            field=models.FloatField(default=0.0, verbose_name='missile accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='missiles_damage',
            field=models.FloatField(default=0.0, verbose_name='missile damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='plasma_accuracy',
            field=models.FloatField(default=0.0, verbose_name='plasma accuracy', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='plasma_damage',
            field=models.FloatField(default=0.0, verbose_name='plasma damage dealt', editable=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playersnapshot',
            name='plasma_efficiency',
            field=models.FloatField(default=0.0, verbose_name='plasma efficiency', editable=False),
            preserve_default=True,
        ),
    ]
