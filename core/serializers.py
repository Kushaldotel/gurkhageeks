from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Categories

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
class categorySerializer(serializers.ModelSerializer):  

    class Meta:
        model = Categories
        fields = '__all__'


class PostSerializerread(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    categories=categorySerializer(read_only=True,many=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'tags', 'categories', 'created_at', 'updated_at']