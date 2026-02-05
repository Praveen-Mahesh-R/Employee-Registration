from django.shortcuts import render
from .models import Employee
import datetime

# Create your views here.
def emp_list(request):
    emp = Employee.objects.order_by('join_date')
    return render(request, 'emp_reg/emp_list.html', {'emp' : emp})