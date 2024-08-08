from django.urls import path,include
from .views import PostsViewset,CategoriesView,Recentpostsview
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('recentposts/',Recentpostsview.as_view(), name='recentposts'),
    path('', include(router.urls)),
]