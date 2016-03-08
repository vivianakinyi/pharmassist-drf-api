from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from .models import Pharmacy, Drugs, Prices


class PharmacySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Pharmacy
        geo_field = "point"
        fields = ('id', 'no', 'name', 'town', 'street', 'county', 'landmarks',
                  'drugs')


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drugs


class PriceSerializer(serializers.ModelSerializer):
    drug_name = serializers.ReadOnlyField(source='drug.full_name')
    pharmacy_name = serializers.ReadOnlyField(source='pharmacy.name')

    class Meta:
        model = Prices
