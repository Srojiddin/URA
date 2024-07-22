from django.urls import path

from apps.users.views import (
    IndexView
)
from apps.users.views import register, CustomLoginView, CustomLogoutView, UserProfileView
from . import views
from .views import edit_doctor_profile, delete_doctor_profile



urlpatterns = [
   path('', IndexView.as_view(), name='index'),
   path('account/register/', views.register, name='register'),
   path('account/login/', CustomLoginView.as_view(), name='login'),
   path('account/logout/', CustomLogoutView.as_view(), name='logout'),
   path('profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
   path('profile/edit/', views.edit_profile, name='edit_profile'),
   path('profile/delete/', views.delete_profile, name='delete_profile'),
   path('doctor/<int:pk>/edit/', edit_doctor_profile, name='edit_doctor_profile'),
   path('doctor/<int:pk>/delete/', delete_doctor_profile, name='delete_doctor_profile'),
]