from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render
from django.views import generic
from apps.appointments.models import Appointment, Contact
from django.views.generic import CreateView
from apps.appointments.forms import AppointmentCreateForm, AppointmentDetailForm, AppointmentDeleteForm,ContactForm
from django.urls import reverse_lazy
from apps.appointments.models import Appointment, Doctor, Category
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden

from django.views.generic import TemplateView

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
        return context




class ContactCreateView(LoginRequiredMixin, CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = reverse_lazy('thank_you')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ThankYouView(TemplateView):
    template_name = 'thank_you.html'