# from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from .models import Pharmacy


class PharmacySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Pharmacy
        geo_field = "point"
        fields = ('id', 'no', 'name', 'town', 'street', 'county', 'landmarks')
