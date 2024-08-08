from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers import PostSerializer,PostSerializerread,categorySerializer
from .models import Post,Categories
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser

# Create your views here.
class PostsViewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes= [MultiPartParser]

    def get_queryset(self):
        queryset = Post.objects.all()
        categories= self.request.query_params.get('categories', None)
        if categories is not None:
            queryset = queryset.filter(categories__name=categories)
        return queryset

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return PostSerializerread
        return PostSerializer

    def get_permissions(self):
        if self.action == 'create':
            return [IsAuthenticated()]
        return super().get_permissions()
    
class CategoriesView(APIView):
    def get(self,request):
        categories= Categories.objects.all()
        serializer= categorySerializer(categories,many=True)
        return Response(serializer.data)



class Recentpostsview(APIView):
    def get(self, request):
        posts= Post.objects.all().order_by("-created_at")
        serializer= PostSerializer(posts, many=True)
        return Response(serializer.data)
        
    
            
