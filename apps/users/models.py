from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string


from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('pharmacist', 'Pharmacist'),
        ('patient', 'Patient'),
        ('admin', 'Admin',)
    ]
    
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    specialization = models.CharField(max_length=100, blank=True, null=True)
    image_for_doctor = models.ImageField(upload_to='doctors/', blank=True, null=True)

    def __str__(self):
        return self.username