from rest_framework.serializers import ModelSerializer
from .models import projectshowcase,ProjectShowcaseImage
from rest_framework import serializers


class ProjectShowcaseImageSerializer(ModelSerializer):
    class Meta:
        model = ProjectShowcaseImage
        fields = '__all__'

class ProjectShowcaseSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    images = ProjectShowcaseImageSerializer(many=True, required=False)  

    class Meta:
        model = projectshowcase
        fields = '__all__'

    def validate(self, attrs):
        image= self.context['request'].FILES.getlist('images')
        number_of_images = len(image)
        if number_of_images > 5:
            raise serializers.ValidationError("You can only upload a maximum of 5 images")
        return super().validate(attrs)
    


    def create(self, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        validated_data['user'] = self.context['request'].user
        instance = super().create(validated_data)
        
        for image in images_data:
            ProjectShowcaseImage.objects.create(project_showcase=instance, image=image)
        
        return instance

    def update(self, instance, validated_data):
        images_data = self.context['request'].FILES.getlist('images')
        instance = super().update(instance, validated_data)
        
        if images_data:
            instance.images.all().delete()  # Optionally delete old images if updating
            for image in images_data:
                ProjectShowcaseImage.objects.create(project_showcase=instance, image=image)
        
        return instance
    
   
