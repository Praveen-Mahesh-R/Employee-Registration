from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Role(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Employee(models.Model):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True )
    email = models.EmailField(max_length=200, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL,blank=True,null=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL,blank=True,null=True)
    join_date = models.DateField(null=True, blank=True)
    show = models.BooleanField(default=True)


    def __str__(self):
        return self.first_name

    
# Create your models here.
