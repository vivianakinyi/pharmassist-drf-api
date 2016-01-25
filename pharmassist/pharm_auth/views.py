from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import UserSerializer
from .models import UserProfile


class UserListView(ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserSerializer
