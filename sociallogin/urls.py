from django.urls import path
from .views import GoogleLoginApiView
urlpatterns = [
    path('google/', GoogleLoginApiView.as_view(), name='google_login'),
]
