# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heroes', '0015_move_equipent_bag_bills_fields_to_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='actual_bills',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='bag',
        ),
        migrations.RemoveField(
            model_name='hero',
            name='equipment',
        ),
    ]
