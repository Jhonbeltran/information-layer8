# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-05 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20170503_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date_end',
            field=models.DateTimeField(max_length=255),
        ),
    ]