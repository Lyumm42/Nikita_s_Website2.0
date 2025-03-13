from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUCF(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar')

class CustomUChangeF(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'avatar')