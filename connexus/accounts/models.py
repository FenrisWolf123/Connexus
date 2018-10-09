from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.conf import settings


from .managers import UserManager


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    # email and password are required
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active


class StudentInfo(models.Model):
    CHALLENGERS = 'C'
    PIONEERS = 'P'
    EXPLORERS = 'E'
    VOYAGERS = 'V'

    HOUSE_CHOICES = (
        (CHALLENGERS, 'Challengers'),
        (PIONEERS, 'Pioneers'),
        (EXPLORERS, 'Explorers'),
        (VOYAGERS, 'Voyagers')
    )

    CLASS_CHOICES = list(zip(
        list(range(1, 13)), list(map(str, range(1, 13)))
    ))

    SECTIONS = ['A', 'B', 'C', 'D']

    SECTION_CHOICES = list(zip(SECTIONS, SECTIONS))

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True
    )
    admission_number = models.IntegerField(null=True)
    house = models.CharField(max_length=1, choices=HOUSE_CHOICES)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    grade = models.IntegerField(choices=CLASS_CHOICES)
    section = models.CharField(max_length=1, choices=SECTION_CHOICES)

    def __str__(self):
        return f'{self.first_name} {self.last_name[0]}'

    class Meta:
        ordering = ['grade', 'section']
        verbose_name = 'Student info'
        verbose_name_plural = 'Student info'
