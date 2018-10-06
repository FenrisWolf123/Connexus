from django.urls import path, include
from django.views.generic import TemplateView

from .views import StudentRegistrationView


urlpatterns = [
    path('home/', TemplateView.as_view(template_name='home.html'), name='home'),
    path(
        'register/',
        StudentRegistrationView.as_view(),
        name='register'
    ),
]
