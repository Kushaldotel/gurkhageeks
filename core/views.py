from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers import PostSerializer,PostSerializerread,categorySerializer, CommentSerializer,CommentCreateSerializer
from .models import Post,Categories,PostComments
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status

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
        
class Postcomment(APIView):

    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'PUT']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get(self, request,pk):
        comments= PostComments.objects.filter(post=pk)
        serializer= CommentSerializer(comments, many=True)
        return Response(serializer.data)
    def post(self, request, pk):
        comment_text = request.data.get("comment")
        if not comment_text:
            return Response({"detail": "Comment is required."}, status=status.HTTP_400_BAD_REQUEST)
        post = Post.objects.filter(pk=pk).first()
        if not post:
            return Response({"detail": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
        data = {
            'post': pk,
            'comment': comment_text
        }
        serializer = CommentSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk):
        try:
            comment = PostComments.objects.get(pk=pk)
        except PostComments.DoesNotExist:
            return Response({"detail": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)
        if comment.author != request.user:
            return Response({"detail": "You do not have permission to edit this comment."}, status=status.HTTP_403_FORBIDDEN)
        
        comment_text = request.data.get("comment")
        data = {
            'comment': comment_text
        }
        serializer = CommentCreateSerializer(comment, data=data, partial=True)
        if serializer.is_valid():
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        