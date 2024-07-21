from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

CustomUser = get_user_model()



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
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor')


    def __str__(self):
        return f"{self.name}: {self.choosing_a_specialization}"

    def get_absolute_url(self):
        return reverse('doctors_list', args=[str(self.id)])



class DoctorProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_code = models.CharField(max_length=10, unique=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    image_for_doctor = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.user.username

