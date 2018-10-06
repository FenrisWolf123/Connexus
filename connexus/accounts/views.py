from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.views.generic import RedirectView
from django.urls import reverse_lazy, reverse

from .forms import UserRegistrationForm, UserLoginForm


def logout_view(request):
    logout(request)
    return redirect(reverse('accounts:home'))


class StudentLoginView(View):
    template_name = 'login.html'
    form_class = UserLoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'test': None})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, username=email, password=password)
            login(request, user)
            return redirect('accounts:home')

        return render(request, self.template_name, {'form': form, 'test': 'hello'})


class StudentRegistrationView(View):
    template_name = 'register.html'
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(request, user)
            return redirect('accounts:home')

        return render(request, self.template_name, {'form': form})
