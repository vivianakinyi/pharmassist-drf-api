from rest_framework import serializers
from .models import Drugs


class DrugSerializer(serializers.ModelSerializer):

    class Meta:
        model = Drugs
