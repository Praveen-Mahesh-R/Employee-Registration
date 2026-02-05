from django.db import models
import datetime

class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    join_date = models.DateField(default=datetime.date.today)

    def re(self):
        self.join_date = datetime.date.today()
        self.save()
    def __str__(self):
        return self.first_name

    
# Create your models here.
