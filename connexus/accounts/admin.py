from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import StudentUser

# Register your models here.
admin.site.register(StudentUser, UserAdmin)
