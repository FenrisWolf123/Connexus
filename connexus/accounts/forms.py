# accounts.forms.py
from django import forms

from .models import User
from .admin import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control form-control-alternative',
                'placeholder': 'Email',
            }
        ),
    )

    password1 = forms.CharField(
        label='password1',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-alternative',
                'placeholder': 'Password',
            }
        )
    )

    password2 = forms.CharField(
        label='password1',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirm Password',
            }
        )
    )

    icons = {
        'password1': 'ni ni-lock-circle-open',
        'password2': 'ni ni-lock-circle-open',
        'email': 'ni ni-email-83'
    }


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }
        ),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
            }
        )
    )

    icons = {
        'password': 'ni ni-lock-circle-open',
        'email': 'ni ni-email-83'
    }
