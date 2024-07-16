from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Appointment

# class AppointmentCreateForm(forms.ModelForm):
    # class Meta:
    #     model = Appointment
    #     fields = ['fullname', 'choosing_a_doctor', 'date_of_reservation']
      



from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Appointment

class AppointmentCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['fullname', 'choosing_a_doctor', 'date_of_reservation', 'time_of_reservation']

    def clean_date_of_reservation(self):
        date_of_reservation = self.cleaned_data['date_of_reservation']
        if date_of_reservation < timezone.now().date():
            raise ValidationError('Вы не можете записаться на прошедшую дату.')
        return date_of_reservation

    def clean_time_of_reservation(self):
        time_of_reservation = self.cleaned_data['time_of_reservation']
        if isinstance(time_of_reservation, str):
            try:
                time_of_reservation = timezone.datetime.strptime(time_of_reservation, '%H:%M').time()
            except ValueError:
                raise ValidationError('Некорректный формат времени. Используйте HH:MM.')
        
        # Check if an appointment already exists for the chosen date and time
        date_of_reservation = self.cleaned_data.get('date_of_reservation')
        if date_of_reservation and time_of_reservation:
            reservation_datetime = timezone.datetime.combine(date_of_reservation, time_of_reservation)
            reservation_datetime = timezone.make_aware(reservation_datetime)

            if Appointment.objects.filter(date_of_reservation=date_of_reservation, time_of_reservation=time_of_reservation).exists():
                raise ValidationError('Запись на прием на это время уже существует.')

            # Check if time is within the allowed range (8:00 - 12:30, 13:30 - 17:00) excluding extended lunch break (12:30 - 13:30)
            start_morning = timezone.datetime.combine(date_of_reservation, timezone.datetime.min.time()) + timezone.timedelta(hours=8)
            end_morning = timezone.datetime.combine(date_of_reservation, timezone.datetime.min.time()) + timezone.timedelta(hours=12, minutes=30)
            start_afternoon = timezone.datetime.combine(date_of_reservation, timezone.datetime.min.time()) + timezone.timedelta(hours=13, minutes=30)
            end_afternoon = timezone.datetime.combine(date_of_reservation, timezone.datetime.min.time()) + timezone.timedelta(hours=17)

            # Check if the time is not in the lunch break (12:30 - 13:30)
            if not ((start_morning.time() <= time_of_reservation < end_morning.time()) or (start_afternoon.time() <= time_of_reservation <= end_afternoon.time())):
                raise ValidationError('Запись возможна только с 8:00 до 12:30 и с 13:30 до 17:00.')

            # Check if there's at least 15 minutes gap between appointments
            if Appointment.objects.filter(date_of_reservation=date_of_reservation, time_of_reservation__gte=reservation_datetime - timezone.timedelta(minutes=15), time_of_reservation__lt=reservation_datetime + timezone.timedelta(minutes=15)).exists():
                raise ValidationError('Между записями должен быть перерыв как минимум 15 минут.')

        return time_of_reservation

    def clean(self):
        cleaned_data = super().clean()
        date_of_reservation = cleaned_data.get('date_of_reservation')
        time_of_reservation = cleaned_data.get('time_of_reservation')

        if date_of_reservation and time_of_reservation:
            reservation_datetime = timezone.datetime.combine(date_of_reservation, time_of_reservation)
            reservation_datetime = timezone.make_aware(reservation_datetime)

            if reservation_datetime <= timezone.now():
                raise ValidationError('Вы не можете записаться на прошедшее время.')

        return cleaned_data



class AppointmentDetailForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class AppointmentDeleteForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'




