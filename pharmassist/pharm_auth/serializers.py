from rest_framework import serializers
# from rest_auth.serializers import UserDetailsSerializer
from .models import UserProfile


class UserSerializer(serializers.ModelSerializer):

    # first_name = serializers.ReadOnlyField(source='user.first_name')
    # last_name = serializers.ReadOnlyField(source='user.last_name')
    # user_email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = UserProfile


# class UserSerializer(UserDetailsSerializer):
#     category = serializers.CharField(source="UserProfile.category")

#     class Meta(UserDetailsSerializer.Meta):
#         fields = UserDetailsSerializer.Meta.fields + ('category',)

#     def update(self, instance, validated_data):
#         profile_data = validated_data.pop('UserProfile', {})
#         category = profile_data.get('category')

#         instance = super(UserSerializer, self).update(instance, validated_data)
#         # get and update user profile
#         profile = instance.UserProfile
#         if profile_data and category:
#             profile.category = category
#             profile.save()
#         return instance
