from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import projectshowcase
from .serializers import ProjectShowcaseSerializer

# Create your views here.


class ProjectShowcaseView(ModelViewSet):
    queryset = projectshowcase.objects.all()
    serializer_class = ProjectShowcaseSerializer
    http_method_names = ["get", "post", "patch", "delete"]
    parser_classes = [MultiPartParser]
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method in ["GET"]:
            return [AllowAny()]
        else:
            return [IsAuthenticated()]
