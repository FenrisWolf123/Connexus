# accounts.forms.py
from django import forms

from .models import User
from .admin import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    pass


class UserLoginForm(forms.Form):
    email = forms.EmailField(label='Email', widget=forms.EmailInput)
    password = forms.CharField(
        label='Password', widget=forms.PasswordInput)
