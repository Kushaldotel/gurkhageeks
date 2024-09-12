import django_filters
from .models import Roadmap

class RoadmapFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')  # Case-insensitive search

    class Meta:
        model = Roadmap
        fields = ['title']