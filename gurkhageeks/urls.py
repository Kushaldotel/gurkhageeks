"""
URL configuration for gurkhageeks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


api_patterns = [
    path("auth/", include("authentication.urls")),
    path("blog/", include("core.urls")),
    path('contacts/', include("contacts.urls")),
    path('projectshowcase/', include("projectshowcase.urls")),
    path('quiz/', include("quiz.urls")),
    path('accounts/', include('userprofile.urls')),
    path('roadmaps/', include('roadmaps.urls')),
]

urlpatterns = [
    path('secretadmin/', admin.site.urls),
    path('api/v1/', include(api_patterns)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)