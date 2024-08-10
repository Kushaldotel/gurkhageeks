from django.urls import path,include
from .views import PostsViewset,CategoriesView,Recentpostsview, Postcomment,PostLikeDislikeView
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('recentposts/',Recentpostsview.as_view(), name='recentposts'),
    path('postcomment/<int:pk>/',Postcomment.as_view(), name='postcomment'),
    path("postlike/<int:pk>/",PostLikeDislikeView.as_view(), name="postlikedislike"),
    path('', include(router.urls)),
]