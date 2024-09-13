from django.urls import path,include
from .views import PostsViewset,CategoriesView,Recentpostsview,PostLikeDislikeView,Mostlikedpost,Latestpostview,WeekelyPost,CommentViewSet
from rest_framework.routers import DefaultRouter
router= DefaultRouter()
router.register('', PostsViewset)


urlpatterns = [
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('recentposts/',Recentpostsview.as_view({'get': 'list'}), name='recentposts'),
    # path('postcomment/<int:pk>/',Postcomment.as_view(), name='postcomment'),
    # path('comments/<int:pk>/replies/', CommentReplyView.as_view(), name='comment-replies-list-create'),
    # path('replies/<int:pk>/', CommentReplyDetailView.as_view(), name='comment-reply-detail'),

    # # URL for fetching and posting comments for a specific post
    # path('posts/<int:pk>/comments/', Postcomment.as_view(), name='post-comments'),
    # # URL for updating (patching) an existing comment by its ID
    # path('comments/<int:pk>/', Postcomment.as_view(), name='update-comment'),

    path("postlike/<int:pk>/",PostLikeDislikeView.as_view(), name="postlikedislike"),
    path("mostlikedpost/",Mostlikedpost.as_view(), name="mostlikedpost"),
    path("latestposts/",Latestpostview.as_view(),name="latestposts"),
    path("postthisweek/",WeekelyPost.as_view(), name= "thisweekpost"),

    path('posts/<int:post_id>/comments/', CommentViewSet.as_view({'post': 'create', 'get': 'list'})),  # Create and list comments
    path('comments/<int:pk>/', CommentViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'})),  # Update and delete comments


    path('', include(router.urls)),
]