# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-07-08 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kshamata_users', '0011_auto_20170708_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='dob',
            field=models.DateField(default=datetime.datetime(2017, 7, 8, 16, 47, 30, 456186, tzinfo=utc)),
        ),
    ]