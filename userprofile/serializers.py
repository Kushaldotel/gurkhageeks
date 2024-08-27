from django.contrib.auth import get_user_model
from rest_framework import serializers
from core.models import Post
from projectshowcase.models import projectshowcase
from rest_framework.reverse import reverse
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
        request = self.context.get('request')  # Get the request object from the context
        blogs = Post.objects.filter(author=obj).values('id', 'title', 'thumbnail', 'created_at')
        # Construct full URLs for each blog
        blog_list = [
            {
                'id': blog['id'],
                'title': blog['title'],
                'thumbnail': blog['thumbnail'],
                'created_at': blog['created_at'],
                'url': request.build_absolute_uri(reverse('post-detail', kwargs={'pk': blog['id']}))  # Adjust 'post-detail' to your actual URL name
            }
            for blog in blogs
        ]
        return blog_list

    def get_total_project_showcase(self, obj):
        return projectshowcase.objects.filter(user=obj ).count()

    def get_project_showcase(self, obj):
        request = self.context.get('request')  # Get the request object from the context
        project_showcases = projectshowcase.objects.filter(user=obj).values('id', 'name', 'created_at')
        # Construct full URLs for each project showcase
        project_showcase_list = [
            {
                'id': showcase['id'],
                'name': showcase['name'],
                'created_at': showcase['created_at'],
                'url': request.build_absolute_uri(reverse('projectshowcase-detail', kwargs={'pk': showcase['id']}))  # Adjust 'projectshowcase-detail' to your actual URL name
            }
            for showcase in project_showcases
        ]
        return project_showcase_list

class UserUpdateSerailizer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['id', 'first_name','last_name', 'profile_pic', 'bio', 'website']



    