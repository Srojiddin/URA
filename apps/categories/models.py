from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=55,verbose_name="Специализация")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

