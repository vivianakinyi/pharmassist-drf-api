from rest_framework import serializers

from .models import Drugs
from .models import Prices


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drugs


class PriceSerializer(serializers.ModelSerializer):
    drug_name = serializers.ReadOnlyField(source='drug.full_name')
    pharmacy_name = serializers.ReadOnlyField(source='pharmacy.name')

    class Meta:
        model = Prices
