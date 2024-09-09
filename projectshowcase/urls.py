from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ProjectShowcaseView

router = DefaultRouter()
router.register("", ProjectShowcaseView, basename="projectshowcase")

urlpatterns = [
    path("", include(router.urls)),
]
