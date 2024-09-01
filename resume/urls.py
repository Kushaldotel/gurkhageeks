from django.urls import path
from .views import ResumeFeedbackViewSet
urlpatterns = [
    path("feedback/",ResumeFeedbackViewSet.as_view({'post': 'create'}), name="feedback"),

]