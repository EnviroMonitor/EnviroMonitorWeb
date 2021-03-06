# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-07 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20170406_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metering',
            name='hw_id',
            field=models.CharField(blank=True, default=None, help_text='Unique ID of station hardware that created Metering.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='metering',
            name='pm01',
            field=models.FloatField(blank=True, default=None, help_text='PM 0.1 in ug/m^3', null=True),
        ),
        migrations.AlterField(
            model_name='metering',
            name='temp_out1',
            field=models.FloatField(blank=True, default=None, help_text='Outside temperature sensor1, in C.', null=True),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='hw_id',
            field=models.CharField(blank=True, default=None, help_text='Unique ID of station hardware that created Metering.', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='pm01',
            field=models.FloatField(blank=True, default=None, help_text='PM 0.1 in ug/m^3', null=True),
        ),
        migrations.AlterField(
            model_name='meteringhistory',
            name='temp_out1',
            field=models.FloatField(blank=True, default=None, help_text='Outside temperature sensor1, in C.', null=True),
        ),
    ]
