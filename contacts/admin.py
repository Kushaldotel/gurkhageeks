from django.contrib import admin
from .models import ContactsForm

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=['name','email','subject','phone_number','datetime']
    ordering=['-datetime']


admin.site.register(ContactsForm,ContactAdmin)