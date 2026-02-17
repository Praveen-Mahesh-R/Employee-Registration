from django.shortcuts import render
from .models import Employee, Role, Department
from .forms import EmpForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import datetime

# Create your views here.
def emp_list(request):
    emp = Employee.objects.filter(show = True).order_by('join_date')
    return render(request, 'emp_reg/emp_list.html', {'emp' : emp})

# def emp_search(request):
      

def emp_new(request):

    if request.method == "POST":
        form = EmpForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            if post.join_date is None:
                post.join_date = datetime.date.today()
            post.save()
            dept = get_object_or_404(Department,pk = post.department_id)
            role = get_object_or_404(Role,pk = post.role_id)

            post.emp_id = dept.dep_id + str(f"{role.pk:02}") + str(f"{post.pk:03}")
            post.save()
            return redirect('emp_list')
    else:
        form = EmpForm()
    return render(request, 'emp_reg/emp_new.html', {'form': form})

def emp_edit(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    dept_old = get_object_or_404(Department,pk = post.department_id)
    role_old = get_object_or_404(Role,pk = post.role_id)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            if post.join_date is None:
                post.join_date = datetime.date.today()
            dept = get_object_or_404(Department,pk = post.department_id)
            role = get_object_or_404(Role,pk = post.role_id)
            if dept_old.dep_id is not dept.dep_id:
                post.emp_id = dept.dep_id + str(f"{role.pk:02}") + post.emp_id[4:]
            elif role_old.pk is not role.pk:
                post.emp_id = post.emp_id[:2] + str(f"{role.pk:02}") + post.emp_id[4:]
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
    post.show = False
    post.save()
    return redirect('emp_list')

def load_roles(request):
    department_id = request.GET.get('department')
    roles = Role.objects.filter(department_id=department_id).all()
    return render(request, 'emp_reg/role_list.html', {'roles': roles})

