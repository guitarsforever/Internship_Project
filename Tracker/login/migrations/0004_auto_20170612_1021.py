# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-12 14:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20170609_2114'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreadiness',
            name='Status_Details',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Status_Time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='completed',
            field=login.models.IntegerRangeField(default=0),
        ),
    ]