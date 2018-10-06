from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login

from .forms import UserRegistrationForm


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
            return redirect('home')

        return render(request, self.template_name, {'form': form})
