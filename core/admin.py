from django.contrib import admin

# Register your models here.
from .models import Categories, Post, PostComments, Postinteraction

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(PostComments)
admin.site.register(Postinteraction)
