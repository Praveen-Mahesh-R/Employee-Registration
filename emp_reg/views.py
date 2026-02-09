from django.shortcuts import render
from .models import Employee
from .forms import EmpForm
from django.shortcuts import render, get_object_or_404
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
            if post.join_date is None:
                post.join_date = datetime.date.today()
            post.save()
            return redirect('emp_list')
    else:
        form = EmpForm()
    return render(request, 'emp_reg/emp_edit.html', {'form': form})

def emp_edit(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.join_date is None:
                post.join_date = datetime.date.today()
            post.save()
            return redirect('emp_list')
    else:
        form = EmpForm(instance=post)
    return render(request, 'emp_reg/emp_edit.html', {'form': form})

def emp_remove(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    return render(request, 'emp_reg/emp_remove.html', {'emp': post})

def emp_delete(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    post.delete()
    return redirect('emp_list')