# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-03-09 11:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_auto_20180309_1148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessrecord',
            old_name='url',
            new_name='name',
        ),
    ]