from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser

User = get_user_model()








class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role')


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Подтвердите пароль', widget=forms.PasswordInput)
    
    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Кардиолог'),
        ('Gynaecologist', 'Гинеколог'),
        ('Neurologist', 'Невролог'),
        ('Ophthalmologist', 'Офтальмолог'),
        ('Paediatrician', 'Педиатр'),
        ('General Practitioner', 'Общий врач'),
    ]

    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    specialization = forms.ChoiceField(choices=SPECIALIZATION_CHOICES, required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone_number', 'avatar', 'role', 'specialization')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError(
                "This account is inactive.",
                code='inactive',
            )




class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=True, label='Номер телефона')
    avatar = forms.ImageField(required=False, label='Аватар')
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'avatar', 'password1', 'password2', 'role']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("Имя пользователя уже занято.")
        return username

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        return phone_number

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают.")

        return cleaned_data


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'role', 'avatar']
