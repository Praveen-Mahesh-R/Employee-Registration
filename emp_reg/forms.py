from django import forms

from .models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('first_name','last_name','email','department','role','join_date')