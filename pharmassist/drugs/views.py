from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import DrugSerializer
from .models import Drugs


class DrugListView(ListCreateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer


class DrugDetailView(RetrieveUpdateAPIView):
    queryset = Drugs.objects.all()
    serializer_class = DrugSerializer
