# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0020_auto_20170405_2150'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='state',
            field=models.CharField(choices=[('AC', 'Active'), ('IN', 'Inactive')], default='AC', max_length=2),
        ),
    ]