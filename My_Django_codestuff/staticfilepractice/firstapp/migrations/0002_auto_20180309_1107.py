# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-09 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='name',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='webpage',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
