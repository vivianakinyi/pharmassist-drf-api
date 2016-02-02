from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .models import Location
from .serializers import LocationSerializer


class LocationListView(ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetailView(RetrieveUpdateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
