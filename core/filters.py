from dataclasses import field
import django
import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name="title",lookup_expr='icontains')
    categories = django_filters.CharFilter(field_name="categories__id", lookup_expr="exact")
    author = django_filters.CharFilter(field_name="author__first_name", lookup_expr="exact")
    tags = django_filters.CharFilter(field_name="tags", lookup_expr="icontains")


    class Meta:
        model = Post
        fields = ['title','categories', 'author', 'tags']
