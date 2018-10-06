from django.urls import path, include, reverse
from django.views.generic import TemplateView, RedirectView

from .views import StudentRegistrationView, logout_view, StudentLoginView

app_name = 'accounts'
urlpatterns = [
    path('home/', TemplateView.as_view(template_name='test.html'), name='home'),
    path(
        'register/',
        StudentRegistrationView.as_view(),
        name='register'
    ),
    path('login/', StudentLoginView.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
]
