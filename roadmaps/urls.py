from django.urls import path
from .views import RoadmapListView, RoadmapDetailView

urlpatterns = [
    path('list/', RoadmapListView.as_view(), name='roadmap-list'),
    path('<int:pk>/', RoadmapDetailView.as_view(), name='roadmap-detail'),
]
