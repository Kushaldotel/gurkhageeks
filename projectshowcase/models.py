from django.db import models
from django.contrib.auth import get_user_model
user= get_user_model()

# Create your models here.

class projectshowcase(models.Model):
    name=models.CharField(max_length=100)
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
