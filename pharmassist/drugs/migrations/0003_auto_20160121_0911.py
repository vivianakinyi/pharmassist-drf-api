# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 09:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drugs', '0002_drugs_form'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drugs',
            name='code',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]