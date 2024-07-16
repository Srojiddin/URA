from django import forms
from apps.cart.models import Favorite

from .models import Item


class AddToFavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        fields = ['product']



class AddToCartForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['quantity']

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product', None)
        self.cart = kwargs.pop('cart', None)
        super().__init__(*args, **kwargs)
        if self.product:
            self.instance.product = self.product
        if self.cart:
            self.instance.cart = self.cart