from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework import filters

from .models import Pharmacy
from .serializers import PharmacySerializer


class PharmacyListView(ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,)
    filter_fields = ('name', 'street', 'town', 'county', 'landmarks')
    search_fields = ('name', 'street', 'town', 'county', 'landmarks')
    ordering_fields = '__all__'


class PharmacyDetailView(RetrieveUpdateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
