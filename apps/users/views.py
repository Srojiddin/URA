from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .forms import CustomAuthenticationForm
from .forms import CustomUserRegisterForm
from .forms import CustomUserRegisterForm, EditProfileForm, CustomAuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.doctors.models import Doctor
from django.views.generic import  TemplateView

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from apps.appointments.models import Appointment

from django.contrib.auth.decorators import login_required

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser




class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()

        return context



def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Регистрация успешна.')
                return redirect('index')  # Замените 'index' на нужный URL
            except IntegrityError:
                form.add_error('username', 'Имя пользователя уже занято.')
        else:
            messages.error(request, 'Регистрация не удалась. Пожалуйста, исправьте ошибки ниже.')
    else:
        form = CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/')


class CustomLoginView(LoginView):
    template_name = 'user/login.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # This method is called when form is valid
        login(self.request, form.get_user())
        messages.success(self.request, 'Вы успешно вошли в систему.')
        return redirect('/')



class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            doctor = self.request.user.doctor  # Получаем связанного доктора
            context['appointments'] = Appointment.objects.filter(choosing_a_doctor=doctor)
        except Doctor.DoesNotExist:
            context['appointments'] = []
        context['user'] = self.request.user
        return context


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form
    }
    return render(request, 'user/edit_profile.html', context)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your profile was successfully deleted!')
        return redirect('/')
    return render(request, 'user/delete_profile.html')

    # return render(request, 'user/profile.html', {'user': request.user})

