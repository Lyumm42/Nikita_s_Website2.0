from django import forms
from django.contrib.auth.forms import UserCreationForm
from apps.users.models import User


class RegistrationForm(UserCreationForm):
    model = User
    fields = ('email', 'password1', 'password2')


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)