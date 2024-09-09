from django.urls import path

from .views import RoadmapDetailView, RoadmapListView

urlpatterns = [
    path("list/", RoadmapListView.as_view(), name="roadmap-list"),
    path("<int:pk>/", RoadmapDetailView.as_view(), name="roadmap-detail"),
]
