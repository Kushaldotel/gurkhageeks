from django.contrib import admin
from .models import CustomUser, TermsandServices

# Register your models here.
admin.site.register(CustomUser)

admin.site.register(TermsandServices)