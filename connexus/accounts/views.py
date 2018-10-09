from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.views.generic import RedirectView
from django.urls import reverse_lazy, reverse

from .forms import UserRegistrationForm, UserLoginForm, UserInfoRegistrationForm
from .models import StudentInfo


def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:home'))


class StudentLoginView(View):
    template_name = 'form.html'
    form_class = UserLoginForm
    message = 'Sign in with'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'message': self.message})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
            else:
                form.add_error('email', 'Wrong email or/and password')
                return render(request, self.template_name, {'form': form, 'message': self.message})
            return redirect('accounts:home')

        return render(request, self.template_name, {'form': forms, 'message': self.message})


class StudentRegistrationView(View):
    template_name = 'form.html'
    form_class = UserRegistrationForm
    second_form_class = UserInfoRegistrationForm
    message = 'Register'

    def get(self, request, *args, **kwargs):
        user_form = self.form_class()
        info_form = self.second_form_class()
        return render(request, self.template_name, {'form': user_form, 'form2': info_form, 'message': self.message})

    def post(self, request, *args, **kwargs):
        user_form = self.form_class(request.POST)
        info_form = self.second_form_class(request.POST)
        if user_form.is_valid() and info_form.is_valid():
            no = info_form.cleaned_data['admission_number']

            # check if this admission number is exists or not
            if not StudentInfo.objects.filter(admission_number=no):
                # This admssion number doesn't exist
                info_form.add_error(
                    'admission_number', 'No such admission number exists.'
                )
                return render(request, self.template_name, {'form': user_form,  'message': self.message})

            # check if admission numberhas been registered or not
            try:
                boi = StudentInfo.objects.get(
                    admission_number=no, user__isnull=True)
                user = user_form.save()
                boi.user = user
                boi.save()
                login(request, user)
                return redirect('accounts:home')
            except:
                info_form.add_error(
                    'admission_number', f'{no} is already a registered account. Have you used your own admission number?'
                )
                return render(request, self.template_name, {'form': user_form, 'form2': info_form, 'message': self.message})

        return render(request, self.template_name, {'form': user_form, 'form2': info_form, 'message': self.message})
