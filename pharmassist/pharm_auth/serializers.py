from rest_framework import serializers
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    first_name = serializers.ReadOnlyField(source='user.first_name')
    last_name = serializers.ReadOnlyField(source='user.last_name')
    user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = UserProfile
