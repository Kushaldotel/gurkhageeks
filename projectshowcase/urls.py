
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import ProjectShowcaseView


router = DefaultRouter()
router.register('', ProjectShowcaseView, basename='projectshowcase')

urlpatterns = [
    path('', include(router.urls)),
]
