from django.db import models
from django.utils.text import slugify

# Create your models here.
class Roadmap(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    resource_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=100, unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug= slugify(self.title)
        super(Roadmap, self).save(*args, **kwargs)


class RoadmapImage(models.Model):

    roadmap = models.ForeignKey(Roadmap, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="roadmap", blank=False, null=True)
    image_no = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.roadmap.title