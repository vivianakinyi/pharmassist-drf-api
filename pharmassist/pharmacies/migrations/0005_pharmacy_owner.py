# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-28 12:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0004_auto_20160403_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='owner',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
