from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework import filters

from .serializers import DrugSerializer
from .models import Drugs


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
