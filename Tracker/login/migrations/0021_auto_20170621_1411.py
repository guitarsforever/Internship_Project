# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-21 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0020_auto_20170621_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectkickoffmeetingstatus',
            name='completed_date',
            field=models.DateField(null=True),
        ),
    ]
