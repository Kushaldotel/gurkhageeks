from django.contrib import admin

# Register your models here.
from .models import projectshowcase,ProjectShowcaseImage


admin.site.register(projectshowcase)
admin.site.register(ProjectShowcaseImage)