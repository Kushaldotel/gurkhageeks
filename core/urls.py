from django.urls import path,include
from .views import PostsViewset,CategoriesView,Recentpostsview, Postcomment,PostLikeDislikeView,Mostlikedpost,Latestpostview,WeekelyPost,CommentReplyView,CommentReplyDetailView
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('recentposts/',Recentpostsview.as_view({'get': 'list'}), name='recentposts'),
    path('postcomment/<int:pk>/',Postcomment.as_view(), name='postcomment'),
    path('comments/<int:pk>/replies/', CommentReplyView.as_view(), name='comment-replies-list-create'),
    path('replies/<int:pk>/', CommentReplyDetailView.as_view(), name='comment-reply-detail'),
    path("postlike/<int:pk>/",PostLikeDislikeView.as_view(), name="postlikedislike"),
    path("mostlikedpost/",Mostlikedpost.as_view(), name="mostlikedpost"),
    path("latestposts/",Latestpostview.as_view(),name="latestposts"),
    path("postthisweek/",WeekelyPost.as_view(), name= "thisweekpost"),
    path('', include(router.urls)),
]