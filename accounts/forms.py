from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, SetPasswordForm

class RegForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']

class ChangePassForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1','new_password2']
