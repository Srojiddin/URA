
from django.db import models
from apps.doctors.models import Doctor


class Schedule(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    time = models.CharField(max_length=100)  
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
        # verbose_name='Выбор врача'
    )
    day = models.CharField(max_length=12, choices=DAY_CHOICES)
    experience = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.choosing_a_doctor} ({self.time})"
