from rest_framework.generics import ListAPIView
from .models import Quiz, categories, Question, Answer, QuizTaker, Response
from .serializers import (QuizSerializer,CategoriesSerializer)
from django_filters.rest_framework import DjangoFilterBackend

class CategoriesListView(ListAPIView):

        queryset = categories.objects.all()
        serializer_class = CategoriesSerializer

class QuizListView(ListAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']