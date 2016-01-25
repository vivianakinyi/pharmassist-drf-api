from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyListView(ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class PharmacyDetailView(RetrieveUpdateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
