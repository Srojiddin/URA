from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


from apps.products.models import Medicine
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE,
        related_name='cart',
        verbose_name='Пользователь'
    )

    def __str__(self):
        return f"{self.user}"

    def get_total_sum(self):
        return sum(i.get_subtotal_sum() for i in self.items_cart.all())

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class Item(models.Model):
    product = models.ForeignKey(
        Medicine,
        on_delete=models.CASCADE,
        related_name='cart_item',
        verbose_name='Продукт'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество',
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE,
        related_name='items_cart',
        verbose_name='Корзина'
    )

    def get_subtotal_sum(self):
        return int(self.quantity * self.product.price)

    def __str__(self):
        return f"{self.product.title}"

    class Meta:
        verbose_name = 'Элемент корзина'
        verbose_name_plural = 'Элемент корзины'


class Favorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Medicine, on_delete=models.CASCADE)
