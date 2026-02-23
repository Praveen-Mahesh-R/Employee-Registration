from django import forms
from django.forms import ModelForm
from .models import Employee, Role

class DateInput(forms.DateInput):
    input_type = 'date'

# class EmpSearch(forms.forms):
    
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['employee'].queryset = Employee.objects.all()
#         if 'search' in self.data:
#             try:
#                 department_id = int(self.data.get('department'))
#                 self.fields['role'].queryset = Role.objects.filter(department_id=department_id).order_by('name')
#             except (ValueError, TypeError):
#                 pass  
#         elif self.instance.pk:
#             self.fields['role'].queryset = self.instance.department.role_set.order_by('name')


class EmpForm(ModelForm):


    class Meta:
        model = Employee
        exclude = ["show","emp_id"]
        widgets = {
            'join_date' : DateInput(),
            'date_of_birth' : DateInput()
        }
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['role'].queryset = Role.objects.filter(department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  
        elif self.instance.pk:
            self.fields['role'].queryset = self.instance.department.role_set.order_by('name')

    def clean(self):

        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        department = cleaned_data.get('department')
        role = cleaned_data.get('role')
        dob = cleaned_data.get('date_of_birth')

        if not first_name:
            self.add_error('first_name', "First Name should not be empty")
        if not email:
            self.add_error('email', "Email should not be empty")
        if not department:
            self.add_error('department', "Please choose a Department")
        if not role:
            self.add_error('role', "Please choose a Role")
        if not dob:
            self.add_error('date_of_birth', "Please choose a Date of Birth")

        # if Employee.objects.filter(email=email).exists():
        #     self.add_error('email','This email already exists!')

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



