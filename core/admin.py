from django.contrib import admin

# Register your models here.
from .models import Post, Categories

admin.site.register(Post)
admin.site.register(Categories)
