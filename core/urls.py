from django.urls import path,include
from .views import PostsViewset,CategoriesView
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('', include(router.urls)),
]