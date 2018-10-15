from django.urls import path, include, reverse
from django.views.generic import TemplateView, RedirectView

from .views import home_page_view

app_name = 'home'
urlpatterns = [
    path('', home_page_view, name='homepage'),
]
