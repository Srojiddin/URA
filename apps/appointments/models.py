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


class Contact(models.Model):
    ...



# class 