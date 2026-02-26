from django.shortcuts import render
from .models import Employee, Role, Department
from django.contrib.auth.models import User
from .forms import EmpForm
from accounts.forms import RegForm, ChangePassForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Q
import datetime


#home page, shows employee list if logged in as admin or show employee details if logged in as employee

def emp_home(request):
    
    usertype = request.user.is_superuser
    if usertype:
                order = request.GET.get('order_by','join_date')
                emp = Employee.objects.filter(show = True).order_by(order)
                query = request.GET.get("q", None)
                
                if query:
                    emps = Employee.objects.filter(
                        Q(first_name__icontains = query)|Q(last_name__icontains = query)|Q(email__icontains = query)|Q(department__name__icontains = query)|Q(role__name__icontains = query)|Q(emp_id__icontains = query)
                        ).order_by(order).filter(show = True)
                    return render(request, 'emp_reg/emp_list.html', {'emp' : emps})
                return render(request, 'emp_reg/emp_list.html', {'emp' : emp})
    elif hasattr(request.user, 'email'):
        email = request.user.email
        emp = get_object_or_404(Employee, email=email)
        return render(request, 'emp_reg/emp_detail.html', {'emps' : emp})
    else:
        return render(request,'emp_reg/base.html',{})

#admin views
#show list of deleted employee entries

def emp_del_list(request):
    order = request.GET.get('order_by','join_date')
    emp = Employee.objects.filter(show = False).order_by(order)
    query = request.GET.get("q", None)
    
    if query:
        emps = Employee.objects.filter(
            Q(first_name__icontains = query)|Q(last_name__icontains = query)|Q(email__icontains = query)|Q(department__name__icontains = query)|Q(role__name__icontains = query)|Q(emp_id__icontains = query)
            ).order_by(order).filter(show = False)
        return render(request, 'emp_reg/emp_del_list.html', {'emp' : emps})
    return render(request, 'emp_reg/emp_del_list.html', {'emp' : emp})


#to add new employees and provide and account for them      

def emp_new(request):
    print("hello")
    if request.method == "POST":
        form = EmpForm(request.POST)
        rform = RegForm(request.POST)
        if form.is_valid() and rform.is_valid():
            post = form.save(commit=False)
            rpost = rform.save(commit=False)
            if post.join_date is None:
                post.join_date = datetime.date.today()
            rpost.username = rpost.username.lower()
            post.save()
            rpost.email = post.email
            rpost.save()
            messages.success(request, 'Employee Added and account created!')
            dept = get_object_or_404(Department,pk = post.department_id)
            role = get_object_or_404(Role,pk = post.role_id)

            post.emp_id = dept.dep_id + str(f"{role.pk:02}") + str(f"{post.pk:03}")
            post.save()
            return redirect('emp_home')
    else:
        form = EmpForm()
        rform = RegForm()
    return render(request, 'emp_reg/emp_new.html', {'form': form, 'rform': rform})

#to edit existing employee details

def emp_edit(request, pk):
    obj = get_object_or_404(Employee, pk=pk)
    obj2 = get_object_or_404(User, email = obj.email)
    post = EmpForm(instance = obj)
    dept_old = get_object_or_404(Department,pk = obj.department_id)
    role_old = get_object_or_404(Role,pk = obj.role_id)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=obj)
        if form.is_valid():
            post = form.save(commit=False)
            # post.author = request.user
            if post.join_date is None:
                post.join_date = datetime.date.today()
            obj2.email = post.email
            obj2.save()
            dept = get_object_or_404(Department,pk = post.department_id)
            role = get_object_or_404(Role,pk = post.role_id)
            if dept_old.dep_id is not dept.dep_id:
                post.emp_id = dept.dep_id + str(f"{role.pk:02}") + post.emp_id[4:]
            elif role_old.pk is not role.pk:
                post.emp_id = post.emp_id[:2] + str(f"{role.pk:02}") + post.emp_id[4:]
            post.save()
            return redirect('emp_home')
    else:
        form = EmpForm(instance=obj)
    return render(request, 'emp_reg/emp_edit.html', {'form': form})

#to remove employee from list (moves them to deleted list)

def emp_remove(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    return render(request, 'emp_reg/emp_remove.html', {'emp': post})

def emp_delete(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    post.show = False
    post.save()
    return redirect('emp_home')

#to restore employee back into list (moves them back to main list)

def emp_restore(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    return render(request, 'emp_reg/emp_restore.html', {'emp': post})

def emp_rest_conf(request, pk):
    post = get_object_or_404(Employee, pk=pk)
    post.show = True
    post.save()
    return redirect('emp_del_list')

#user/employee views
#show employee details

def emp_detail(request):
    email = request.user.email
    emp = get_object_or_404(Employee, email = email) 
    return render(request, 'emp_reg/emp_detail.html', {'emps' : emp})

#allow employee to edit their details

def emp_user_edit(request):
    email = request.user.email
    obj = get_object_or_404(Employee, email = email)
    obj2 = get_object_or_404(User, email = email)
    post = EmpForm(instance = obj)
    dept_old = get_object_or_404(Department,pk = obj.department_id)
    role_old = get_object_or_404(Role,pk = obj.role_id)
    if request.method == "POST":
        form = EmpForm(request.POST, instance=obj)
        if form.is_valid():
            post = form.save(commit=False)
            if post.join_date is None:
                post.join_date = datetime.date.today()
            obj2.email = post.email
            obj2.save()
            dept = get_object_or_404(Department,pk = post.department_id)
            role = get_object_or_404(Role,pk = post.role_id)
            if dept_old.dep_id is not dept.dep_id:
                post.emp_id = dept.dep_id + str(f"{role.pk:02}") + post.emp_id[4:]
            elif role_old.pk is not role.pk:
                post.emp_id = post.emp_id[:2] + str(f"{role.pk:02}") + post.emp_id[4:]
            post.save()
            return redirect('emp_home')
    else:
        form = EmpForm(instance=obj)
    return render(request, 'emp_reg/emp_edit.html', {'form': form})

#allow users to change password
            
def update_password(request):
    if request.user.is_authenticated:
        current_user = request.user
        if request.method == "POST":
            form = ChangePassForm(current_user,request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your Password has been resetted")
                return redirect('/')
            else:
                errormsg = ""
                for error in list(form.errors.values()):
                    errormsg = errormsg + error
                context = {"error": errormsg}
                return render(request, 'emp_reg/update_password.html',context)
        else:
            form = ChangePassForm(current_user)
            return render(request, 'emp_reg/update_password.html', {'form':form})
    else:
        messages.success(request, 'You are not logged in!')
        return redirect('emp_home')
    
#view for admin to see see their own details

def admin_detail(request):
    email = request.user.email
    emp = get_object_or_404(Employee, email=email)
    return render(request, 'emp_reg/emp_detail.html', {'emps' : emp})

#loads list of roles based on what dept is selected when creating or editing employees

def load_roles(request):
    department_id = request.GET.get('department')
    roles = Role.objects.filter(department_id=department_id).all()
    return render(request, 'emp_reg/role_list.html', {'roles': roles})

