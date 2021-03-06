# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-17 16:34
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainserver', '0003_auto_20170317_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alarm',
            name='hours_active_beg',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='hours_active_end',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(24)]),
        ),
        migrations.AlterField(
            model_name='localization',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='information',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sensor',
            name='localization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainserver.Localization'),
        ),
    ]
