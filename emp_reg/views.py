from django.shortcuts import render
from .models import Employee
from .forms import EmpForm
from django.shortcuts import redirect
import datetime

# Create your views here.
def emp_list(request):
    emp = Employee.objects.order_by('join_date')
    return render(request, 'emp_reg/emp_list.html', {'emp' : emp})

def emp_new(request):
    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('emp_list')
    else:
        form = EmpForm()
    return render(request, 'emp_reg/emp_edit.html', {'form': form})