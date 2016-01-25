from django.db import models


class Pharmacy(models.Model):
    pharm_code = models.CharField(max_length=15, unique=True, blank=True)
    pharm_name = models.CharField(max_length=60)
    town = models.CharField(max_length=60)
    street = models.CharField(max_length=60)
    county = models.CharField(max_length=60, default='NAIROBI')
