from django.db import models


class Drugs(models.Model):
    code = models.CharField(max_length=15, unique=True)
    common_name = models.CharField(max_length=60)
    scientific_name = models.CharField(max_length=60, blank=True)
    price = models.FloatField(blank=True)
    form = models. CharField(max_length=20, blank=True)
