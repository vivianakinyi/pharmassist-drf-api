# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0003_auto_20160121_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='scientific_name',
            field=models.CharField(blank=True, max_length=60),
        ),
    ]
