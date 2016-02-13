from django.contrib.gis.db import models


class Pharmacy(models.Model):
    no = models.CharField(max_length=15, unique=True, blank=True)
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    landmarks = models.CharField(max_length=200, blank=True, null=True)
    point = models.PointField(null=True, blank=True)
