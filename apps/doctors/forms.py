from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.crypto import get_random_string
from .models import Doctor, CustomUser, DoctorProfile  # Убедитесь, что DoctorProfile импортирован
from .models import Doctor

# class CustomUserRegisterForm(UserCreationForm):
#     class Meta:
#         model = CustomUser
#         fields = ('username', 'email', 'password1', 'password2', 'role')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         if commit:
#             user.save()
#             if user.role == 'doctor':
#                 DoctorProfile.objects.create(
#                     user=user,
#                     profile_code=get_random_string(10)  # Генерируем случайный код
#                 )
#         return user

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role')

class DoctorCreateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'choosing_a_specialization', 'phone_number', 'email', 'image_for_doctor')

class DoctorUpdateForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'choosing_a_specialization', 'phone_number', 'email', 'image_for_doctor')

class DoctorDeleteForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = []  # Можно оставить пустым, если нет дополнительных полей


# class DoctorProfileForm(forms.ModelForm):
#     class Meta:
#         model = DoctorProfile
#         fields = ['phone_number', 'email', 'image_for_doctor']

# class DoctorEditForm(forms.ModelForm):
#     class Meta:
#         model = DoctorProfile
#         fields = ['phone_number', 'email', 'image_for_doctor']



class DoctorSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Имя')
    specialization = forms.ChoiceField(choices=[('', '---')]+Doctor.SPECIALIZATION_CHOICES, required=False, label='Специализация')
