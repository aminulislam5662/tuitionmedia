from django.db import models

# Create your models here.
class tuitor(models.Model):
    name= models.TextField(max_length=255)
    age = models.TextField(max_length=255)
    phone = models.TextField(max_length=255)
    email = models.TextField(max_length=255)
    study = models.TextField(max_length=255)
    subject = models.TextField(max_length=255)
    adress = models.TextField(max_length=255)