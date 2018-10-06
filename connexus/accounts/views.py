from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, logout
from django.views.generic import RedirectView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import AuthenticationForm

from .forms import UserRegistrationForm


def logout_view(request):
    logout(request)
    print(reverse('accounts:home'))
    return redirect(reverse('accounts:home'))


class StudentLoginView(View):
    template_name = 'login.html'
    form_class = AuthenticationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'test': None})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.get_user()
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
