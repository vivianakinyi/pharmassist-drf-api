from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer


from .models import Pharmacy, Drugs, Prices


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drugs
class PriceSerializer(serializers.ModelSerializer):
    drug_name = serializers.ReadOnlyField(source='drug.display_name')
    pharmacy_name = serializers.ReadOnlyField(source='pharmacy.name')
    county = serializers.ReadOnlyField(source='pharmacy.county')
    town = serializers.ReadOnlyField(source='pharmacy.town')
    recommended_price = serializers.ReadOnlyField(source='drug.recommended_price')

    class Meta:
        model = Prices

class PharmacySerializer(GeoFeatureModelSerializer):
    drugs = DrugSerializer(many=True, read_only=True)
    pharmacy_prices = PriceSerializer(many=True, read_only=True)

    class Meta:
        model = Pharmacy
        geo_field = "point"
        auto_bbox = True
        fields = ('id', 'no', 'name', 'town', 'street', 'county', 'landmarks',
                  'owner', 'updated', 'drugs', 'pharmacy_prices',)



