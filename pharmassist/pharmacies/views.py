from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework import filters

from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyListView(ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('name', 'street', 'town', 'county', 'landmarks')


class PharmacyDetailView(RetrieveUpdateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
