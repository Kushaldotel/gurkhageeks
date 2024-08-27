from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Post
from projectshowcase.models import projectshowcase
User=get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    total_blogs= serializers.SerializerMethodField()
    blogs= serializers.SerializerMethodField()

    total_project_showcase= serializers.SerializerMethodField()
    project_showcase= serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=['id', 'email', 'first_name','last_name', 'profile_pic', 'bio', 'website', 'total_blogs', 'blogs', 'total_project_showcase', 'project_showcase']

    def get_total_blogs(self, obj):
        return Post.objects.filter(author=obj).count()

    def get_blogs(self, obj):
        return Post.objects.filter(author=obj ).values('id', 'title', 'thumbnail', 'created_at')

    def get_total_project_showcase(self, obj):
        return projectshowcase.objects.filter(user=obj ).count()

    def get_project_showcase(self, obj):
        return projectshowcase.objects.filter(user=obj ).values('id', 'name','created_at')

class UserUpdateSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id', 'first_name','last_name', 'profile_pic', 'bio', 'website']



    