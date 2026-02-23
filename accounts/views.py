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

# def register(request):
#     if request.method == 'POST':
#         form = RegForm(request.POST) 
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.username = user.username.lower()
#             user.save()
#             messages.success(request, 'You have singed up successfully.')
#             login(request, user)
#             return redirect('posts')
#         else:
#             return render(request, 'users/register.html', {'form': form})
# def csrf_failure(request, reason=""):
#     ctx = {'message': 'hello'}
#     return render(request, 'registration/signup.html', ctx)


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
            # if isadmin.is_superuser:
            #     return render(request, 'emp_reg/emp_list.html',{'emp' : emp_list})
            # else:
            #     emp = get_object_or_404(Employee, email = isadmin.email)
            #     return render(request, 'emp_reg/emp_detail.html', {'emps' : emp})
    # form = forms.AuthenticationForm()
    # return render(request, 'registration/login.html',{})


