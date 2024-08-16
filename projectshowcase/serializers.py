from rest_framework.serializers import ModelSerializer
from .models import projectshowcase
from rest_framework import serializers

class ProjectShowcaseSerializer(ModelSerializer):
    user= serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = projectshowcase
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        return super().create(validated_data)
    
   
