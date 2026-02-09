from django import forms

from .models import Employee

class EmpForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        model.join_date = forms.DateField(
            widget=forms.DateInput(format='%d/%m/%Y'),
            input_formats=('%d/%m/%Y')
        )
