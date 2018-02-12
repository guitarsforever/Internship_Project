# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-28 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import login.models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0038_auto_20170712_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeviceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Completed', login.models.IntegerRangeField(default=0)),
                ('Created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]