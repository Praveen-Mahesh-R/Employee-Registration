from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, forms
from django.shortcuts import render, redirect, get_object_or_404
from emp_reg.models import Employee, Role, Department
from django.contrib.auth.models import User

#login page view 

def LoginView(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)
        if user is None:
            context = {"error": "Invalid username or password"}
            # form = login(request, user)
            # email = usertype.email
            # messages.success(request, f' Welcome {username} !')
            return render(request, 'registration/login.html',context)
        login(request, user)
        return redirect('/')
    return render(request,'registration/login.html',{})

#logout page view

def logout_check(request):
    email = request.user.email
    emp = get_object_or_404(Employee, email=email)
    return render(request, 'registration/logout.html', {'emps' : emp})



