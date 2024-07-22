from django.shortcuts import render
from django.views import generic
from django.utils.timezone import make_aware
from datetime import time
from apps.schedules.models import Schedule

from apps.schedules.forms import ScheduleCreateForm
from .forms import ScheduleCreateForm

from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic

from apps.schedules.models import Schedule

from apps.schedules.forms import ScheduleCreateForm
from django.views.generic.edit import CreateView,DeleteView

class ScheduleListView(generic.ListView):
    model = Schedule
    template_name = 'time-table.html'
    context_object_name = "schedules"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Группировка расписания по докторам
        doctors = {}
        for schedule in Schedule.objects.all():
            doctor = schedule.choosing_a_doctor
            if doctor not in doctors:
                doctors[doctor] = {'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': [], 'Saturday': [], 'Sunday': []}
            doctors[doctor][schedule.day].append(schedule)

        context['doctors'] = doctors
        context['days_of_week'] = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        context['form'] = ScheduleCreateForm()
        
        return context




  


class ScheduleCreateView(CreateView):
    model = Schedule
    form_class = ScheduleCreateForm
    template_name = 'schedule_form.html'
    success_url = reverse_lazy('schedule_list')



class ScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'schedule_confirm_delete.html'
    success_url = reverse_lazy('schedule_list')