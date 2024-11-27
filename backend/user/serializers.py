from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username', 'password', 'email', 'birthday', 'phone_number', 'profile_picture']

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

