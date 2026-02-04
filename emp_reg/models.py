from django.db import models
from django.utils import timezone

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    joindate = models.DateTimeField(default=timezone.now)

    
# Create your models here.
