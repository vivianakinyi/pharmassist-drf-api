from django.contrib.gis.db import models


class Drugs(models.Model):
    rxcui = models.CharField(max_length=20, null=False, default="")
    generic_rxcui = models.CharField(max_length=20, blank=True)
    tty = models.CharField(max_length=20, blank=False, default="")
    full_name = models.CharField(max_length=3000, blank=False, default="")
    rxn_dose_form = models.CharField(max_length=100, blank=False, default="")
    full_generic_name = models.CharField(max_length=3000, blank=False, default="")
    brand_name = models.CharField(max_length=500, blank=True)
    display_name = models.CharField(max_length=3000, blank=False, default="")
    route = models.CharField(max_length=100, blank=False, default="")
    new_dose_form = models.CharField(max_length=100, blank=False, default="")
    strength = models.CharField(max_length=500, blank=False, default="")
    suppress_for = models.CharField(max_length=30, blank=True)
    display_name_synonym = models.CharField(max_length=500, blank=True)
    is_retired = models.CharField(max_length=20, blank=True)
    sxdg_rxcui = models.CharField(max_length=20, blank=True)
    sxdg_tty = models.CharField(max_length=20, blank=True)
    sxdg_name = models.CharField(max_length=3000, blank=True)
    psn = models.CharField(max_length=3000, blank=True)

    def __str__(self):
        return "{0} : {1}".format(self.tty, self.display_name)


class Pharmacy(models.Model):
    no = models.CharField(max_length=15, unique=True, blank=True)
    name = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    landmarks = models.CharField(max_length=200, blank=True, null=True)
    point = models.PointField(null=True, blank=True)
    drugs = models.ManyToManyField(Drugs, through='Prices')

    def __str__(self):
        return "{0} : {1}".format(self.name, self.town)


class Prices(models.Model):

    from pharmacies.models import Pharmacy

    drug = models.ForeignKey(Drugs)
    pharmacy = models.ForeignKey(Pharmacy)
    price = models.DecimalField(decimal_places=2, max_digits=8, blank=True,
                                null=True)

    class Meta:
        unique_together = ('pharmacy', 'drug',)
