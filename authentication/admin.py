from django.contrib import admin

from .models import CustomUser, Organisation, TermsandServices

# Register your models here.
admin.site.register(CustomUser)

admin.site.register(TermsandServices)

admin.site.register(Organisation)
