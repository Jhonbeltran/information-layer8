# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 22:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20170327_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='timezone',
            field=models.CharField(choices=[('(UTC-0500) America/Bogota', 'America/Bogota'), ('(UTC-0800) America/Los_Angeles', 'America/Los_Angeles')], default='America/Bogota', max_length=255),
        ),
    ]
