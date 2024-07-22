from collections import defaultdict
# from django.template.defaultfilters import slugify

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views import View
from django.contrib.auth import get_user_model
from apps.blogs.models import Blog
from apps.doctors.models import Doctor
from django.views.generic.edit import CreateView,UpdateView
from apps.categories.models import Category
from django.core.exceptions import PermissionDenied
from apps.users.forms import CustomUserCreationForm
from apps.doctors.forms import DoctorCreateForm, DoctorUpdateForm, DoctorDeleteForm

from django.contrib.auth.decorators import login_required
from .forms import DoctorSearchForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser
# from .models import DoctorProfile, Appointment


        
class DoctorCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'doctors/doctor_create.html'
    success_url = reverse_lazy('doctors_list')

    def form_valid(self, form):
        if not self.request.user.is_staff:
            raise PermissionDenied("Вы не имеете права создавать врачей.")
        
        response = super().form_valid(form)
        
        # Проверка роли и создание профиля врача при создании пользователя
        if form.cleaned_data['role'] == 'doctor':
            if not Doctor.objects.filter(user=self.object).exists():
                Doctor.objects.create(
                    user=self.object,
                    name=form.cleaned_data['name'],
                    choosing_a_specialization=form.cleaned_data['specialization'],
                    phone_number=form.cleaned_data['phone_number'],
                    email=form.cleaned_data['email'],
                    image_for_doctor=form.cleaned_data.get('image_for_doctor')  # Убедитесь, что вы передаете изображение
                )
        
        return response

class DoctorListView(generic.ListView):
    model = Doctor
    template_name = 'doctors.html'
    context_object_name = "doctors"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = DoctorCreateForm()  


        context['cardiologists'] = Doctor.objects.filter(choosing_a_specialization='Cardiologist')
        context['gynaecologists'] = Doctor.objects.filter(choosing_a_specialization='Gynaecologist')
        context['neurologists'] = Doctor.objects.filter(choosing_a_specialization='Neurologist')
        context['ophthalmologists'] = Doctor.objects.filter(choosing_a_specialization='Ophthalmologist')
        context['paediatricians'] = Doctor.objects.filter(choosing_a_specialization='Paediatrician')
        context['practitioners'] = Doctor.objects.filter(choosing_a_specialization='General Practitioner')

        return context


class DoctorDetailView(generic.DetailView):
    model = Doctor
    template_name = 'doctors-detail.html'
    context_object_name = 'doctors'
    pk_url_kwarg = 'pk'

    def doctor_detail(request, pk):
        doctor = get_object_or_404(Doctor, pk=pk)
        return render(request, 'doctor_detail.html', {'doctor': doctor})

class DoctorUpdateView(UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'doctors/doctor_update.html'
    success_url = reverse_lazy('doctors_list')

    def form_valid(self, form):
        user_email = form.cleaned_data.get('email')
        User = get_user_model()
        # Проверка только для нового email (если email был изменен)
        if User.objects.filter(email=user_email).exclude(id=self.object.user.id).exists():
            form.add_error('email', 'Пользователь с таким email уже существует.')
            return super().form_invalid(form)
        return super().form_valid(form)


class DoctorDeleteView(generic.DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_delete.html'
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctors_list')



