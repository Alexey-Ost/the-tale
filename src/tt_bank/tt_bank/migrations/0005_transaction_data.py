# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2019-09-08 08:23
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tt_bank', '0004_auto_20180119_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default='{}'),
        ),
    ]