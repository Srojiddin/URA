from django.contrib import admin

from apps.appointments.models import Appointment,Contact

admin.site.register(Appointment)
admin.site.register(Contact)
