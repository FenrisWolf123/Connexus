from django.db import models
from django.contrib.auth.models import User


class StudentUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    info = models.OneToOnefield(
        StudentInfo,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )


class StudentInfo(models.Model):
    CHALLENGERS = 'C'
    PIONEERS = 'P'
    VOYAGERS = 'V'
    EXPLORERS = 'E'
    HOUSE_CHOICES = (
        (CHALLENGERS, 'Challengers'),
        (PIONEERS, 'Pioneers'),
        (EXPLORERS, 'Explorers'),
        (VOYAGERS, 'Voyagers'),
    )

    admission_number = models.PositiveIntegerField(null=True)
    house = models.CharField(
        max_length=1,
        choices=HOUSE_CHOICES,
        default=CHALLENGERS
    )
