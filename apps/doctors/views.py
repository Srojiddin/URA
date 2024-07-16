from collections import defaultdict
# from django.template.defaultfilters import slugify

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.views import View

from apps.blogs.models import Blog
from apps.doctors.models import Doctor
from apps.categories.models import Category
from apps.doctors.forms import DoctorCreateForm, DoctorUpdateForm, DoctorDeleteForm





class DoctorCreateView(generic.CreateView):
    model = Doctor
    form_class = DoctorCreateForm
    template_name = 'doctors/doctor_create.html'
    success_url = reverse_lazy('doctors_list')
    context_object_name = "doctors.html"



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


class DoctorUpdateView(generic.UpdateView):
    model = Doctor
    form_class = DoctorUpdateForm
    template_name = 'doctors/doctor_update.html'
    success_url = 'doctors.html'


class DoctorDeleteView(generic.DeleteView):
    model = Doctor
    template_name = 'doctors/doctor_delete.html'
    context_object_name = 'doctor'
    success_url = reverse_lazy('doctors_list')

