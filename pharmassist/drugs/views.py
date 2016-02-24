from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import filters

from .serializers import DrugSerializer, PriceSerializer
from .models import Drugs, Prices


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


class PriceDetailView(RetrieveUpdateAPIView):
    queryset = Prices.objects.all()
    serializer_class = PriceSerializer
