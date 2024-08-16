from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import ProjectShowcaseSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import projectshowcase
from rest_framework.parsers import MultiPartParser


# Create your views here.

class ProjectShowcaseView(ModelViewSet):
    queryset= projectshowcase.objects.all()
    serializer_class = ProjectShowcaseSerializer
    http_method_names = ['get', 'post', 'patch', 'delete']
    parser_classes= [MultiPartParser]

    def get_permissions(self):
        if self.request.method in ['GET']:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
   

    