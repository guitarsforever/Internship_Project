# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-06 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0035_reference_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreadiness',
            name='Task1_dependent_task',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='announcements',
            name='post',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='callcentertraining',
            name='Task1_Name',
            field=models.CharField(blank=True, default='Create Training: Agents', max_length=100),
        ),
        migrations.AlterField(
            model_name='callcentertraining',
            name='Task2_Name',
            field=models.CharField(blank=True, default='Training Expectation Rollout', max_length=100),
        ),
        migrations.AlterField(
            model_name='callcentertraining',
            name='Task3_Name',
            field=models.CharField(blank=True, default='Training the trainer', max_length=100),
        ),
        migrations.AlterField(
            model_name='callcentertraining',
            name='Task4_Name',
            field=models.CharField(blank=True, default='Train: Agents', max_length=100),
        ),
        migrations.AlterField(
            model_name='callcentertraining',
            name='Task5_Name',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
