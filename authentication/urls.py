# urls.py
from django.urls import path
from .views import RegisterView, LoginView, LogoutView,confirm_registration,ProfileView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("confirm/<str:uidb64>/<str:token>/",confirm_registration,name="confirm_registration"),
    path("profile/",ProfileView.as_view(),name="profile")

]
