# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20170612_1021'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='Device_Category',
            field=models.CharField(choices=[('HE', 'HE'), ('HA', 'HA'), ('MOBILE', 'Mobile')], default='', max_length=10),
        ),
    ]
