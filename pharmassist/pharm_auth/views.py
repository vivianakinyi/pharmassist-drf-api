from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from rest_framework import filters

from .serializers import UserSerializer
from .models import UserProfile


class UserListView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)


class UserDetailView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
