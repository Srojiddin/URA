from django.contrib.auth import get_user_model
from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.crypto import get_random_string
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.conf import settings


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
    image_for_doctor = models.ImageField(upload_to='doctor_images/')
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile')

    def __str__(self):
        return f"{self.name}: {self.choosing_a_specialization}"



@receiver(post_save, sender=CustomUser)
def create_doctor_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'Doctor':
        if not Doctor.objects.filter(user=instance).exists():
            Doctor.objects.create(
                user=instance,
                name=instance.username,  # Укажите необходимые поля
                choosing_a_specialization=instance.specialization,
                phone_number=instance.phone_number,
                email=instance.email,
                image_for_doctor=instance.avatar
            )


