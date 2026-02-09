from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    join_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.first_name

    
# Create your models here.
