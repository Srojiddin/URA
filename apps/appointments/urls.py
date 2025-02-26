from django.urls import path
from apps.appointments.views import AppointmentList, AppointmentCreateView, AppointmentDetail, AppointmentUpdate, AppointmentDelete, ContactCreateView





urlpatterns = [

    path('appointment/', AppointmentList.as_view(), name='appointment-list'),
    path('create/appointments', AppointmentCreateView.as_view(), name='create-appointments'),
    path('appointments/<int:pk>/', AppointmentDetail.as_view(), name='appointment-detail'),
    path('appointments/<int:pk>/update/', AppointmentUpdate.as_view(), name='appointment-update'),
    path('appointments/<int:pk>/delete/', AppointmentDelete.as_view(), name='appointment-delete'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]



