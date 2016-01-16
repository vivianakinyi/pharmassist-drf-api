from django.contrib.auth.models import User, Group
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView

from .serializers import UserSerializer, GroupSerializer


class UserListView(ListCreateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class UserDetailView(RetrieveUpdateAPIView):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupListView(ListCreateAPIView):
    queryset = Group.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer


class GroupDetailView(RetrieveUpdateAPIView):
    queryset = Group.objects.all().order_by('-date_joined')
    serializer_class = GroupSerializer


# class User(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer


# class GroupViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializer
