# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0002_auto_20170719_1543'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='specialproduct',
            options={'permissions': (('is_strategic', 'Is Strategic'),)},
        ),
    ]
