from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveUpdateDestroyAPIView,)
from rest_framework import filters

from .models import Pharmacy, Drugs, Prices
from .serializers import PharmacySerializer, DrugSerializer, PriceSerializer


class PharmacyListView(ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,)
    filter_fields = ('name', 'street', 'town', 'county', 'landmarks', 'drugs')
    search_fields = ('name', 'street', 'town', 'county', 'landmarks', 'drugs')
    ordering_fields = '__all__'


class PharmacyDetailView(RetrieveUpdateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer


class DrugListView(ListCreateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter,
                       filters.OrderingFilter,)
    filter_fields = ('full_name', 'brand_name', 'display_name',
                     'full_generic_name', 'route',)

    search_fields = ('full_name', 'brand_name', 'display_name',
                     'full_generic_name', 'route',)

    ordering_fields = '__all__'


class DrugDetailView(RetrieveUpdateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer


class PriceListView(ListCreateAPIView):
    queryset = Prices.objects.all()
    serializer_class = PriceSerializer


class PriceDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Prices.objects.all()
    serializer_class = PriceSerializer
