import os
from django.db import models
from django.urls import reverse


class Medicine(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Название",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=None,
    )
    image = models.ImageField(
        upload_to='medicine_images/',
        verbose_name='Изображение', null=True, blank=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создание",
    )


    def __str__(self):
        return self.title
    

    class Meta:
        verbose_name = 'Медикамент'
        verbose_name_plural = 'Медикаменты'


# class ShopSingle(models.Model):
#     ...
#
