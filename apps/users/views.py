from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .forms import CustomAuthenticationForm
from .forms import CustomUserRegisterForm
from .forms import CustomUserRegisterForm, EditProfileForm, CustomAuthenticationForm,DoctorEditProfileForm
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.doctors.models import Doctor
from django.views.generic import  TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from apps.appointments.models import Appointment

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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



# class UserProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'user/profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             doctor = self.request.user.doctor  # Получаем связанного доктора
#             context['appointments'] = Appointment.objects.filter(choosing_a_doctor=doctor)
#         except Doctor.DoesNotExist:
#             context['appointments'] = []
#         context['user'] = self.request.user
#         return context
# class UserProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'user/profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user

#         # Попытка получить профиль врача
#         if hasattr(user, 'rofile'):
#             doctor = user.profile  # Используйте правильное имя обратной связи
#             context['appointments'] = Appointment.objects.filter(choosing_a_doctor=doctor)
#         else:
#             context['appointments'] = []
        
#         context['user'] = user
#         return context


# class UserProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'user/profile.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         user = self.request.user

#         if user.role == 'doctor':
#             # Доктор видит только свои записи
#             doctor_profile = user.doctor_profile if hasattr(user, 'doctor_profile') else None
#             if doctor_profile:
#                 context['appointments'] = Appointment.objects.filter(choosing_a_doctor=doctor_profile)
#             else:
#                 context['appointments'] = []
#         elif user.is_staff:
#             # Администратор видит все записи
#             context['appointments'] = Appointment.objects.all()
#         else:
#             context['appointments'] = []

#         context['user'] = user
#         return context
class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user

        if user.role == 'doctor':
            doctor = Doctor.objects.filter(user=user).first()
            context['appointments'] = Appointment.objects.filter(choosing_a_doctor=doctor) if doctor else []
        elif user.is_staff:
            doctor_appointments = {}
            doctors = Doctor.objects.all()
            for doctor in doctors:
                appointments = Appointment.objects.filter(choosing_a_doctor=doctor)
                doctor_appointments[doctor.id] = {
                    'doctor': doctor,
                    'appointments': appointments
                }
            context['doctor_appointments'] = doctor_appointments
            # Добавьте информацию о пациентах
            context['patients'] = Appointment.objects.values('user').distinct()
        elif user.role == 'pharmacist':
            context['pharmacist_info'] = 'Информация для фармацевта'
        else:
            context['appointments'] = None  # Для других ролей блокируем доступ к записям

        # Добавление сообщения клиенту
        context['message'] = 'Ваш запрос был успешно отправлен. Вы получите ответ на ваш email.'

        context['user'] = user
        return context

        
@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль успешно обновлен.')
            return redirect('profile', pk=request.user.pk)
    else:
        form = EditProfileForm(instance=request.user)

    context = {
        'form': form,
        'profile': request.user
    }
    return render(request, 'user/edit_profile.html', context)


@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Ваш профиль успешно удален!')
        return redirect('/')  # Замените на URL, на который следует перенаправить после удаления профиля

    context = {
        'profile': request.user
    }
    return render(request, 'user/delete_profile.html', context)


@login_required
def edit_doctor_profile(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorEditProfileForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Профиль доктора успешно обновлен.')
            return redirect('profile', pk=doctor.pk)  # Передаем pk
    else:
        form = DoctorEditProfileForm(instance=doctor)

    context = {
        'form': form,
        'doctor': doctor
    }
    return render(request, 'user/edit_doctor_profile.html', context)


@login_required
def delete_doctor_profile(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)

    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Профиль доктора успешно удален!')
        return redirect('doctors_list')  # Замените 'doctor_list' на URL для списка докторов или главной страницы

    context = {
        'doctor': doctor
    }
    return render(request, 'user/delete_doctor_profile.html', context)

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def edit_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form = DoctorForm(request.POST, request.FILES, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('doctors_list')  # Замените на нужный вам URL
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'edit_doctor.html', {'form': form})

@user_passes_test(is_admin)
def delete_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors_list')  # Замените на нужный вам URL
    return render(request, 'confirm_delete_doctor.html', {'doctor': doctor})