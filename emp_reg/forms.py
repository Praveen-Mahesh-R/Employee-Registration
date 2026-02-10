from django import forms
from django.forms import ModelForm
from .models import Employee

class DateInput(forms.DateInput):
    input_type = 'date'

class EmpForm(ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'join_date' : DateInput()
        }
