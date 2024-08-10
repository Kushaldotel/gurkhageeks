from django.urls import path,include
from .views import PostsViewset,CategoriesView,Recentpostsview, Postcomment
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('recentposts/',Recentpostsview.as_view(), name='recentposts'),
    path('postcomment/<int:pk>/',Postcomment.as_view(), name='postcomment'),
    path('', include(router.urls)),
]