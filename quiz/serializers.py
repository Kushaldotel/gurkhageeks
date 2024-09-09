from rest_framework import serializers

from .models import Answer, Question, Quiz, QuizTaker, Response, categories


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = categories
        fields = ["id", "name"]


class QuizSerializer(serializers.ModelSerializer):

    class Meta:
        model = Quiz
        fields = ["id", "name", "description", "category"]
