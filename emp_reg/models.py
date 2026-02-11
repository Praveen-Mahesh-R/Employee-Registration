from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True )
    email = models.EmailField(max_length=200, blank=True)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    join_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.first_name

    
# Create your models here.
