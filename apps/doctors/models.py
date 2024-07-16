# from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.categories.models import Category


from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Doctor(models.Model):
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Gynaecologist', 'Gynaecologist'),
        ('Neurologist', 'Neurologist'),
        ('Ophthalmologist', 'Ophthalmologist'),
        ('Paediatrician', 'Paediatrician'),
        ('General Practitioner', 'General Practitioner'),
    ]

    name = models.CharField(max_length=100, verbose_name='Имя врача')
    choosing_a_specialization = models.CharField(max_length=50, choices=SPECIALIZATION_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image_for_doctor = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return f"{self.name}: {self.choosing_a_specialization}"



