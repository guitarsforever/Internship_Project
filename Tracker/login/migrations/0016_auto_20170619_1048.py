# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0015_productreadinessstatus_product_readiness'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreadiness',
            name='Determine_Field_Test_Req',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Develop_Schedule_Req',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Distribute_Full_List_Of_SKUs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Marketing_Deck_Distribution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Production_Samples',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Project_KickOff_Meeting',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='Receive_PR_Samples',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='User_Manual_Distribution',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productreadiness',
            name='User_Manuals',
            field=models.BooleanField(default=False),
        ),
    ]
