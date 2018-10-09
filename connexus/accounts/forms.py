# accounts.forms.py
from django import forms

from .models import User
from .admin import UserCreationForm


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
            }
        ),
    )

    password1 = forms.CharField(
        label='password1',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )

    password2 = forms.CharField(
        label='password1',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirm Password',
            }
        )
    )

    icons = {
        'password1': 'ni ni-lock-circle-open',
        'password2': 'ni ni-lock-circle-open',
        'email': 'ni ni-email-83'
    }


class UserInfoRegistrationForm(forms.Form):
    admission_number = forms.IntegerField(
        label='admission_number',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Admssion number'
            }
        )
    )

    icons = {
        'admission_number': 'ni ni-lock-circle-open'
    }


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        label='email',
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Email',
            }
        ),
    )
    password = forms.CharField(
        label='password',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Password',
            }
        )
    )

    icons = {
        'password': 'ni ni-lock-circle-open',
        'email': 'ni ni-email-83'
    }
