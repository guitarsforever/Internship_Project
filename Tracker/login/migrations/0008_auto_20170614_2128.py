# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20170614_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
