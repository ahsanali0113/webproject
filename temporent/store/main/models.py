from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = RichTextField()

    def __str__(self):
        return self.name


class Lender(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    phone = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=False)
    address = models.TextField()
    cnic = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=False)
    description = RichTextField()
    price = models.CharField(max_length=255)
    category = RichTextField()
    photo_one = models.ImageField(upload_to='users/')
    photo_two = models.ImageField(upload_to='users/')
    date = models.DateTimeField(blank=True,default=datetime.now)

    def __str__(self):
        return self.first_name
