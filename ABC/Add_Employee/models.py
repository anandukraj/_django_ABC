from django.db import models


# Create your models here.
class Add(models.Model):
    Employee_name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    Address = models.CharField(max_length=5000)
    image = models.CharField(max_length=10000)
