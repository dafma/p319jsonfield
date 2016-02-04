# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 16:40
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Casa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=10)),
                ('datos', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
    ]
