from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Roadmap, RoadmapImage
from .serializers import RoadmapSerializer, RoadmapImageSerializer
from utils.pagination import CustomPageNumberPagination

class RoadmapListView(ListAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer
    pagination_class = CustomPageNumberPagination


class RoadmapDetailView(RetrieveAPIView):
    queryset = Roadmap.objects.all()
    serializer_class = RoadmapSerializer