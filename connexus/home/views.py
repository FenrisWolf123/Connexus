from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url=reverse_lazy('accounts:login'))
def home_page_view(request):
    return render(request, 'home\homepage.html')
