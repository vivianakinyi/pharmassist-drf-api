from rest_framework import serializers
from .models import Patient, Pharmacist


class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient


class PharmacistSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pharmacist
