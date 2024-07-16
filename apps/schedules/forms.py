from django import forms
from apps.schedules.models import Schedule



class ScheduleCreateForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = '__all__'
