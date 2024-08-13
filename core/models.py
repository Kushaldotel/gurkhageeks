from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    
class Post(models.Model):
    title = models.CharField(max_length=200)
    thumbnail=models.ImageField(upload_to="thumbnail", blank=False, null=True)
    content = models.TextField() 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Categories, related_name='posts')
    tags = models.CharField(max_length=100,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class PostComments(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    comment=models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.comment} by {self.author}"

class Postinteraction(models.Model):
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    liked= models.BooleanField(default=False)
    disliked= models.BooleanField(default=False)
    liked_disliked_by= models.ForeignKey(User, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now=True)

    def __str__(self):
        return repr(self.post.title)


