from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from .serializers import (PostSerializer,PostSerializerread,categorySerializer, CommentSerializer,
                          CommentCreateSerializer,postlikedislike,SubscriberSerializer,CommentReplySerializer)
from .models import Post,Categories,PostComments,Postinteraction,CommentReply
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import status
from django.db.models import Count
from django.db import models
from .utils import start_and_end_days_of_week
from .filters import PostFilter
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class PostsViewset(ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    parser_classes = [MultiPartParser]
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    filterset_class = PostFilter

    def get_queryset(self):
        queryset = super().get_queryset()
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



# class Recentpostsview(APIView):
#     def get(self, request):
#         posts= Post.objects.all().order_by("-created_at")
#         serializer= PostSerializerread(posts, many=True)
#         return Response(serializer.data)



class Recentpostsview(ReadOnlyModelViewSet):
    serializer_class = PostSerializerread
    queryset = Post.objects.all().order_by("-created_at")

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


class CommentReplyView(APIView):
    
    def get_permissions(self):
        if self.request.method in ['POST', 'PATCH', 'DELETE']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    def get(self, request, pk):
        # pk here is the comment id
        replies = CommentReply.objects.filter(comment=pk)
        serializer = CommentReplySerializer(replies, many=True)
        return Response(serializer.data)
    
    def post(self, request, pk):
        reply_text = request.data.get("reply")
        if not reply_text:
            return Response({"detail": "Reply is required."}, status=status.HTTP_400_BAD_REQUEST)

        comment = PostComments.objects.filter(pk=pk).first()
        if not comment:
            return Response({"detail": "Comment not found."}, status=status.HTTP_404_NOT_FOUND)

        data = {
            'comment': pk,
            'reply': reply_text,
            'author': request.user.id
        }
        serializer = CommentReplySerializer(data=data)
        if serializer.is_valid():
            reply = serializer.save()
            return Response(CommentReplySerializer(reply).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentReplyDetailView(APIView):
    def get_permissions(self):
        return [IsAuthenticated()]

    def patch(self, request, pk):
        try:
            reply = CommentReply.objects.get(pk=pk)
        except CommentReply.DoesNotExist:
            return Response({"detail": "Reply not found."}, status=status.HTTP_404_NOT_FOUND)
        
        if reply.author != request.user:
            return Response({"detail": "You do not have permission to edit this reply."}, status=status.HTTP_403_FORBIDDEN)
        
        reply_text = request.data.get("reply")
        data = {
            'reply': reply_text
        }
        serializer = CommentReplySerializer(reply, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostLikeDislikeView(APIView):

    def get_permissions(self):
        if self.request.method in ['POST']:
            return [IsAuthenticated()]
        return [AllowAny()]
    def get(self,request, pk):
        post=Post.objects.get(id=pk)
        postinteraction= Postinteraction.objects.filter(post=post.id)
        total_like= postinteraction.filter(liked=True).count()
        total_dislike= postinteraction.filter(disliked=True).count()
        serializer= postlikedislike(postinteraction,many=True)
        data={
            'total_like':total_like,
            'total_dislike':total_dislike,
            'data':serializer.data
        }
        return Response(data)

    def post(self, request, pk):
        post= Post.objects.get(id=pk)
        post_interaction, created= Postinteraction.objects.get_or_create(post=post, liked_disliked_by=request.user)
        data = request.data

        # Validate the input
        if 'liked' not in data and 'disliked' not in data:
            return Response({"error": "No like or dislike value provided."}, status=400)

        if data.get('liked') is not None:
            post_interaction.liked = data['liked']
            post_interaction.disliked = False if data['liked'] else post_interaction.disliked
        elif data.get('disliked') is not None:
            post_interaction.disliked = data['disliked']
            post_interaction.liked = False if data['disliked'] else post_interaction.liked

        post_interaction.save()

        return Response({"liked": post_interaction.liked, "disliked": post_interaction.disliked})


class Mostlikedpost(APIView):
    def get(self, request):
        posts = Post.objects.annotate(likes_count=Count('postinteraction', filter=models.Q(postinteraction__liked=True))).order_by('-likes_count')
        serializer= PostSerializer(posts, many=True)
        return Response(serializer.data)

class Latestpostview(APIView):
    def get(self, request):
        post=Post.objects.all().order_by("-created_at")
        serializer= PostSerializer(post, many=True)
        return Response(serializer.data)

class WeekelyPost(APIView):
    def get(self, request):
        start_of_week, end_of_week= start_and_end_days_of_week()
        post= Post.objects.filter(created_at__range=(start_of_week, end_of_week))
        serializer= PostSerializer(post, many=True)
        return Response(serializer.data)

class SubscribeAPIView(APIView):

    def post(self, request):
        serializer = SubscriberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Thank you for subscribing!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)