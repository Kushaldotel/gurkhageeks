from django.contrib import admin

# Register your models here.
from .models import Post, Categories, PostComments

admin.site.register(Post)
admin.site.register(Categories)
admin.site.register(PostComments)
