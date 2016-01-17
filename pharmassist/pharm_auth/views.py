from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import PatientSerializer, PharmacistSerializer
from .models import Patient, Pharmacist


class PatientListView(ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PatientDetailView(RetrieveUpdateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class PharmacistListView(ListCreateAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class PharmacistDetailView(RetrieveUpdateAPIView):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer
