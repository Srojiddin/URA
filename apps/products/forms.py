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