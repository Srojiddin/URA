from django.urls import path
from . import views

from apps.doctors.views import DoctorCreateView, DoctorListView, DoctorDetailView, DoctorUpdateView, DoctorDeleteView


# from .views import doctor_profile, edit_doctor_profile
# doctor_appointments_view, doctor_profile_edit_view
from django.contrib.auth.decorators import login_required, user_passes_test
from .views import DoctorSearchView


def admin_required(function):
    return user_passes_test(lambda u: u.is_staff)(function)

urlpatterns = [
    path('doctor/create/', DoctorCreateView.as_view(), name='doctor_create'),
    path('doctor/', DoctorListView.as_view(), name='doctors_list'),
    path('doctor/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),
    path('doctor/update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctors/<int:pk>/delete/', DoctorDeleteView.as_view(), name='doctor_delete'),
    path('search/doctors/', DoctorSearchView.as_view(), name='doctor_search'),

]




