from django.shortcuts import render

# Create your views here.
def emp_list(request):
    return render(request, 'emp_reg/emp_list.html', {})