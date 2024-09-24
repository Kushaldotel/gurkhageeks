from rest_framework import serializers

class GoogleLoginSerializer(serializers.Serializer):
    token= serializers.CharField()
    
    