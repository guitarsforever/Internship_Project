# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-25 20:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import general.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=100)),
                ('ProductDescription', models.CharField(default='', max_length=100)),
                ('LaunchDate', models.DateField(blank=True, null=True)),
                ('SRADate', models.DateField(blank=True, null=True)),
                ('TADate', models.DateField(blank=True, null=True)),
                ('UnpackDate', models.DateField(blank=True, null=True)),
                ('completed', general.models.IntegerRangeField(default=0)),
                ('Status', models.CharField(choices=[('On Time', 'On Time'), ('At Risk', 'At Risk'), ('Delayed', 'Delayed')], default='On_Time', max_length=10)),
                ('Archive', models.BooleanField(default=False)),
            ],
            options={
                'permissions': (('is_strategic', 'Is Strategic'),),
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TaskName', models.CharField(blank=True, default='', max_length=100)),
                ('StartDate', models.DateField(blank=True, null=True)),
                ('EndDate', models.DateField(blank=True, null=True)),
                ('CompleteDate', models.DateField(blank=True, null=True)),
                ('DependentTask', models.CharField(blank=True, default='', max_length=250)),
                ('Warning', models.BooleanField(default=False)),
                ('Alert', models.BooleanField(default=False)),
                ('IsPostLaunch', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TaskStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.TextField(default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('Task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.Task')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TeamName', models.CharField(blank=True, default='', max_length=100)),
                ('Poc1', models.CharField(blank=True, default='', max_length=100)),
                ('Poc1_email', models.EmailField(blank=True, default='', max_length=100)),
                ('Poc2', models.CharField(blank=True, default='', max_length=100)),
                ('Poc2_email', models.EmailField(blank=True, default='', max_length=100)),
                ('Time_Delta_For_Warning', models.IntegerField(blank=True, default=7)),
                ('completed', general.models.IntegerRangeField(default=0)),
                ('Status', models.CharField(choices=[('On Time', 'On Time'), ('At Risk', 'At Risk'), ('Delayed', 'Delayed')], default='On_Time', max_length=10)),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.Product')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='general.Team'),
        ),
    ]
