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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Gurkha Geeks API",
        default_version="v1",
        description="API documentation of Gurkha Geeks \n\n\n\n Instruction:\nTo use authenticate api, first login through login api, \
        copy the access code from the response then authorize the api with that access code \n \
            Enter the access code in value field with Bearer at prefix \n\n\n\n Example: Bearer 'access code'",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


api_patterns = [
    path("auth/", include("authentication.urls")),
    path("blog/", include("core.urls")),
    path("contacts/", include("contacts.urls")),
    path("projectshowcase/", include("projectshowcase.urls")),
    path("quiz/", include("quiz.urls")),
    path("accounts/", include("userprofile.urls")),
    path("roadmaps/", include("roadmaps.urls")),
    path("resume/", include("resume.urls")),
    # swagger url
    path(
        "api-documentation/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "api-redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]

urlpatterns = (
    [
        path("secretadmin/", admin.site.urls),
        path("api/v1/", include(api_patterns)),
        path("ckeditor5/", include("django_ckeditor_5.urls")),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
