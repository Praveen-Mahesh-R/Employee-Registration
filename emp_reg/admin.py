from django.contrib import admin
from .models import Employee, Department, Role

admin.site.register(Employee)
# Register your models here.

admin.site.register(Department)
admin.site.register(Role)
