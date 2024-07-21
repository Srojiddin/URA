from django import forms
from .models import Medicine


class MedicineCreateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['title', 'image', 'price',]





class MedicineUpdateForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['title', 'image', 'price',]



class MedicineDeleteForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['title', 'image', 'price',]


class MedicineSearchForm(forms.Form):
    title = forms.CharField(required=False, label='Название')
    price_min = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Цена от')
    price_max = forms.DecimalField(required=False, max_digits=10, decimal_places=2, label='Цена до')