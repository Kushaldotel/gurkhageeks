# from django.contrib import admin

# # Register your models here.
# from .models import Post, Categories, PostComments,Postinteraction

# admin.site.register(Post)
# admin.site.register(Categories)
# admin.site.register(PostComments)
# admin.site.register(Postinteraction)
# admin.py
# admin.py
from django.contrib import admin
from .models import Post, Categories, PostComments, CommentReply, Postinteraction



class PostCommentsInline(admin.TabularInline):
    model = PostComments
    extra = 1


class PostinteractionInline(admin.TabularInline):
    model = Postinteraction
    extra = 1

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'content', 'tags')
    list_filter = ('categories', 'created_at')
    inlines = [PostCommentsInline, PostinteractionInline]

    

admin.site.register(Post, PostAdmin)
admin.site.register(Categories)
admin.site.register(PostComments)
admin.site.register(CommentReply)
admin.site.register(Postinteraction)
