from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Post,Categories,PostComments,Postinteraction,CommentReply,Subscriber

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

class CommentReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentReply
        fields = '__all__'
    


class CommentSerializer(serializers.ModelSerializer):
    author=UserSerializer(read_only=True)
    replies = CommentReplySerializer(many=True, read_only=True)  # Include replies in the comment
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

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ['email']

    def validate_email(self,value):

        if Subscriber.objects.filter(email=value).exists():
            raise serializers.ValidationError("You are already subscribed")
        return value