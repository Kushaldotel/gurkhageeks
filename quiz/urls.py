from django.urls import path
from .views import (QuizListView,CategoriesListView)

urlpatterns = [
    path('categories/', CategoriesListView.as_view(), name='categories-list'),
    path('list/', QuizListView.as_view(), name='quiz-list'),
]
