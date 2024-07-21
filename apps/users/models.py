from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('pharmacist', 'Pharmacist'),
        ('patient', 'Patient'),
    ]
    
    email = models.EmailField(blank=True, null=True, unique=True) 
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    specialization = models.CharField(max_length=100, blank=True, null=True)  # Добавьте это поле, если его нет

    def __str__(self):
        return self.username
