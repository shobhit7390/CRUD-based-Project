from django.db import models

# Create your models here.

class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=50)
    age=models.IntegerField()
    course=models.CharField(max_length=100)