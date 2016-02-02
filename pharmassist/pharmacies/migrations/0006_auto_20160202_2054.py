# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-02 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0005_auto_20160125_1002'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='landmarks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='pharmacy',
            name='county',
            field=models.CharField(max_length=100),
        ),
    ]