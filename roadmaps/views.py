from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from utils.pagination import CustomPageNumberPagination

from .models import Roadmap, RoadmapImage
from .serializers import RoadmapImageSerializer, RoadmapSerializer


class RoadmapListView(ListAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
    pagination_class = CustomPageNumberPagination


class RoadmapDetailView(RetrieveAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
