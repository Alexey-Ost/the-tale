# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-09-05 12:05
from __future__ import unicode_literals

from django.db import migrations
import rels.django


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0007_clan_statistics_refreshed_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='clan',
            name='state',
            field=rels.django.RelationIntegerField(default=0),
        ),
    ]
