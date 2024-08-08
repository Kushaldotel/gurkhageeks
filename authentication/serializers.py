# serializers.py
from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import get_user_model
User=get_user_model()
class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name', 'profile_pic', 'bio', 'website']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            profile_pic=validated_data.get('profile_pic', None),
            bio=validated_data.get('bio', ''),
            website=validated_data.get('website', '')
        )
        return user
    
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','first_name', 'last_name', 'profile_pic', 'bio', 'website']