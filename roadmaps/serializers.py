from rest_framework import serializers

from .models import Roadmap, RoadmapImage


class RoadmapImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadmapImage
        fields = ["image", "image_no"]


class RoadmapSerializer(serializers.ModelSerializer):

    images = RoadmapImageSerializer(many=True, read_only=True)

    class Meta:
        model = Roadmap
        fields = ["title", "description", "steps", "resource_url", "images"]
