from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views import generic
from apps.appointments.models import Appointment
from django.views.generic import CreateView
from apps.appointments.forms import AppointmentCreateForm, AppointmentDetailForm, AppointmentDeleteForm
from django.urls import reverse_lazy
from apps.appointments.models import Appointment, Doctor, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

class AppointmentList(generic.ListView):
    model = Appointment
    template_name = 'appointments/contact.html'
    context_object_name = 'appointments_list'




class AppointmentDetail(generic.DetailView):
    model = Appointment
    form_class = AppointmentDetailForm
    template_name = 'appointments/appointment_detail.html'
    context_object_name = 'appointment'


class AppointmentUpdate(generic.UpdateView):
    model = Appointment
    template_name = 'appointments/appointment_update.html'
    form_class = AppointmentDetailForm


class AppointmentDelete(generic.DeleteView):
    model = Appointment
    form_class = AppointmentDeleteForm
    template_name = 'appointments/appointment_confirm_delete.html'
    context_object_name = 'appointment'
    success_url = reverse_lazy('/')


class ContactListView(generic.ListView):
    model = Appointment


class AppointmentCreateView(LoginRequiredMixin, CreateView):
    model = Appointment
    form_class = AppointmentCreateForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()
        context['categories'] = Category.objects.all()
        return context