from django.db import models

# Create your models here.


class ContactsForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    phone_number = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
