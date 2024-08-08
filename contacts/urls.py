from django.urls import path
from .views import ContactFormView
urlpatterns = [
    path("contactform/", ContactFormView.as_view(), name='contact_form'),
    
]
