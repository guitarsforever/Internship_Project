# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 19:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0029_auto_20170627_1151'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task7Statusfieldservicee',
            new_name='Task7Statusfieldservice',
        ),
        migrations.AlterField(
            model_name='device',
            name='CallCenterOpertaions',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.callcenteropertaions'),
        ),
        migrations.AlterField(
            model_name='device',
            name='CallCenterTraining',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.callcentertraining'),
        ),
        migrations.AlterField(
            model_name='device',
            name='DigitalContent',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.digitalcontent'),
        ),
        migrations.AlterField(
            model_name='device',
            name='FieldService',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.fieldservice'),
        ),
        migrations.AlterField(
            model_name='device',
            name='Parts',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.parts'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ProductReadiness',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.ProductReadiness'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ProductSupport',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.productsupport'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ServiceMarketing',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.servicemarketing'),
        ),
        migrations.AlterField(
            model_name='device',
            name='ServiceTraining',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.servicetraining'),
        ),
        migrations.AlterField(
            model_name='device',
            name='TechSupport',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.techsupport'),
        ),
        migrations.AlterField(
            model_name='device',
            name='VideoContent',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.videocontent'),
        ),
        migrations.AlterField(
            model_name='device',
            name='Warehouse',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='login.warehouse'),
        ),
    ]
