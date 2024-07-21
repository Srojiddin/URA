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
    success_url = reverse_lazy('doctor-list')

    def form_valid(self, form):
        if not self.request.user.is_staff:  # Проверка, является ли пользователь администратором
            raise PermissionDenied("Вы не имеете права создавать врачей.")
        return super().form_valid(form)

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
    template_name = 'doctors-update.htm'
    success_url = reverse_lazy('doctor-list')

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




class DoctorSearchView(View):
    def get(self, request):
        form = DoctorSearchForm()
        return render(request, 'doctor/doctor_search.html', {'form': form, 'doctors': None})

    def post(self, request):
        form = DoctorSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            specialization = form.cleaned_data.get('specialization')

            doctors = Doctor.objects.all()

            if name:
                doctors = doctors.filter(name__icontains=name)

            if specialization:
                doctors = doctors.filter(choosing_a_specialization=specialization)

            return render(request, 'doctor/doctor_search.html', {'form': form, 'doctors': doctors})

        return render(request, 'doctor/doctor_search.html', {'form': form, 'doctors': None})


