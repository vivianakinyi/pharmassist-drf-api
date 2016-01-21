# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-21 08:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drugs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('common_name', models.CharField(max_length=60)),
                ('scientific_name', models.CharField(max_length=60)),
                ('code', models.IntegerField(blank=True)),
                ('price', models.FloatField(blank=True)),
            ],
        ),
    ]