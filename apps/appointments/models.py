from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from apps.doctors.models import Doctor
from apps.categories.models import Category
from apps.doctors.models import Doctor
from django.conf import settings

from django.core.exceptions import ValidationError


class Appointment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    fullname = models.CharField(max_length=100, verbose_name='ФИО')
    choosing_a_doctor = models.ForeignKey(
        Doctor,
        on_delete=models.CASCADE,
    #     verbose_name='Выбор врача'
    )
    date_of_reservation = models.DateField(verbose_name='Дата записи')
    time_of_reservation = models.TimeField(verbose_name='Время записи')

    def __str__(self):
        return f"Запись на прием у {self.choosing_a_doctor} на {self.date_of_reservation} в {self.time_of_reservation}"




def validate_phone_number(value):
        if not value.isdigit():
           raise ValidationError('Номер телефона должен содержать только цифры.')


class Contact(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )
    your_name = models.CharField(max_length=50, verbose_name='Ваше имя')
    your_email = models.EmailField(verbose_name='Ваш Email')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', validators=[validate_phone_number])
    description = models.TextField(max_length=300, verbose_name='Описание')

    def clean(self):
        super().clean()
        if len(self.description) > 150:
            raise ValidationError({'description': 'Описание не должно превышать 150 символов.'})



    def __str__(self):
        return self.your_name