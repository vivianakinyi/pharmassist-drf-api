from rest_framework import serializers

from .models import Drugs
from .models import Prices


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drugs


class PriceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prices
