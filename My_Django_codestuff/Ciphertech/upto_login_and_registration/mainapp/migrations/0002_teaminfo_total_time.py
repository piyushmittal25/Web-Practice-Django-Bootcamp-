# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-26 10:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='teaminfo',
            name='total_time',
            field=models.DurationField(blank=True, default=datetime.timedelta(0)),
        ),
    ]