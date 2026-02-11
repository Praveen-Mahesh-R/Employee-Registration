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

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')

        if not first_name:
            self.add_error('first_name', "First Name should not be empty")
        if not email:
            self.add_error('email', "Email should not be empty")

        
        
        if self.validate(first_name):
            self.add_error('first_name','First Name should not contain numbers or special characters!')
        if self.validate(last_name):
            self.add_error('last_name','Last Name should not contain numbers or special characters!')
        return cleaned_data   
            

    def validate(self,mystring):
        if any(not c.isalnum() for c in mystring):
            return True
        if any(c.isdigit() for c in mystring):
            return True
        return False


