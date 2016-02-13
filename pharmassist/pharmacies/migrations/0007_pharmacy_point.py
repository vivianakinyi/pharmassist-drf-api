# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-06 12:17
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacies', '0006_auto_20160202_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='point',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]