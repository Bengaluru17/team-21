# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-08 16:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kshamata_users', '0008_auto_20170708_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='dob',
            field=models.DateField(default=datetime.datetime(2017, 7, 8, 16, 38, 11, 646427, tzinfo=utc)),
        ),
    ]
