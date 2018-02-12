# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-18 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0005_announcements'),
    ]

    operations = [
        migrations.AddField(
            model_name='defaulttask',
            name='AssignedUser',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AddField(
            model_name='defaulttask',
            name='IsPostLaunch',
            field=models.BooleanField(default=False),
        ),
    ]
