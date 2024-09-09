from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserProfileView

router = DefaultRouter()
# router.register(r'userprofile', UserProfileView, basename='userprofile')


urlpatterns = [
    # path('', include(router.urls)),  # Include the router's URLs
    path(
        "userprofile/",
        UserProfileView.as_view({"get": "list", "patch": "partial_update"}),
        name="userprofile",
    ),
]
