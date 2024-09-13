from django.db import models
from django.contrib.auth import get_user_model
from django_ckeditor_5.fields import CKEditor5Field
from django.utils.text import slugify

User=get_user_model()
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug= models.SlugField(max_length=200, unique=True, blank=True, null=True)
    thumbnail=models.ImageField(upload_to="thumbnail", blank=False, null=True)
    content=CKEditor5Field('Text', config_name='extends')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, related_name='posts')
    tags = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    content= models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='replies')
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content


# class PostComments(models.Model):
#     post= models.ForeignKey(Post, on_delete=models.CASCADE)
#     comment=models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True,related_name='replies')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.comment} by {self.author}"

# class CommentReply(models.Model):
#     comment= models.ForeignKey(PostComments, on_delete=models.CASCADE, related_name='replies')
#     reply= models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.reply} by {self.author}"

class Postinteraction(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    liked= models.BooleanField(default=False)
    disliked= models.BooleanField(default=False)
    liked_disliked_by= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return repr(self.post.title)


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
