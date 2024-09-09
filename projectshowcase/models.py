from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
user= get_user_model()

# Create your models here.

class projectshowcase(models.Model):
    name=models.CharField(max_length=100, verbose_name="name of project")
    slug= models.SlugField(max_length=100, unique=True, null=True, blank=True)
    type_of_project= models.CharField(max_length=100, verbose_name="Type of Project eg.mobileapp, ML")
    description_of_project= models.TextField()
    Challenges_faced= models.TextField()
    suggestion= models.TextField()
    technology_used= models.CharField(max_length=200)
    project_link= models.URLField()
    user= models.ForeignKey(user, on_delete=models.CASCADE, related_name="projectshowcase")
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.name)
        super(projectshowcase,self).save(*args, **kwargs)

class ProjectShowcaseImage(models.Model):
    project_showcase= models.ForeignKey(projectshowcase, on_delete=models.CASCADE, related_name="images")
    image= models.ImageField(upload_to="projectshowcase", blank=False, null=True)

    def __str__(self):
        return self.project_showcase.name
