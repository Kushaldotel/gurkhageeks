from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from .models import Answer, Question, Quiz, QuizTaker, Response, categories
from .serializers import CategoriesSerializer, QuizSerializer


class CategoriesListView(ListAPIView):

    queryset = categories.objects.all()
    serializer_class = CategoriesSerializer


class QuizListView(ListAPIView):

    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category"]
