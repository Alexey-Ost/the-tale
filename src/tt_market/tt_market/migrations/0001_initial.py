# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-08-17 11:45
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogRecord',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('operation_type', models.IntegerField()),
                ('lot_type', models.IntegerField()),
                ('item_type', models.CharField(max_length=32)),
                ('item', models.UUIDField()),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default='{}')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'log_records',
            },
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('item_type', models.CharField(max_length=32)),
                ('item', models.UUIDField()),
                ('price', models.IntegerField()),
                ('account', models.BigIntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'lots',
            },
        ),
    ]