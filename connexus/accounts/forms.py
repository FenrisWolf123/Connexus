# accounts.forms.py
from django import forms

from .models import User
from .admin import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    pass


class UserLoginForm:
    pass
