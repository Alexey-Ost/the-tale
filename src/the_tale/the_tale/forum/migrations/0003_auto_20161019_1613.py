# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-19 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_auto_20150506_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]