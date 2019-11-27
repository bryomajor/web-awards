# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-11-25 14:13
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0002_auto_20191125_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rates',
            name='content',
            field=models.IntegerField(default=0, validators=[10]),
        ),
        migrations.AlterField(
            model_name='rates',
            name='design',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='rates',
            name='usability',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
    ]