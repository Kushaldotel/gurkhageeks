# urls.py
from django.urls import path,include
from .views import (RegisterView, LoginView, LogoutView,confirm_registration,
                    ProfileView,TermsandServicesView, ForgotPassword, ResetPasswordView,OrganisationRegistrationView)

urlpatterns = [
    path('register/', RegisterView.as_view({'post': 'create'}), name='register'),
    path('register/organisation/', OrganisationRegistrationView.as_view(), name='register-organization'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('terms-services/', TermsandServicesView.as_view(), name='terms'),
    path("confirm/<str:uidb64>/<str:token>/",confirm_registration,name="confirm_registration"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path('forgot-password',ForgotPassword.as_view({'post': 'create'}),name='forgot_password'),
    path('reset-password/<str:uidb64>/<str:token>/',ResetPasswordView.as_view({'post': 'create'}),name='reset_password'),
    path('', include('sociallogin.urls'))

]
