# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-20 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0025_auto_20170411_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarmactuator',
            name='alarm',
        ),
        migrations.AddField(
            model_name='alarmactuator',
            name='alarm',
            field=models.ManyToManyField(blank=True, to='mainserver.Alarm'),
        ),
    ]