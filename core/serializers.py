from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Categories,PostComments,Postinteraction

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields=['slug']

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
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    class Meta:
        model = PostComments
        fields = '__all__'

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComments
        fields = '__all__'


# class postlikedislike(serializers.ModelSerializer):
#     # post= PostSerializer(read_only=True)
#     # author= UserSerializer(read_only=True)
#     class Meta:
#         model:Postinteraction
#         fields='__all__'

class postlikedislike(serializers.ModelSerializer):  
    # post= PostSerializer(read_only=True)
    # author= UserSerializer(read_only=True)
    class Meta:
        model = Postinteraction
        fields = '__all__'