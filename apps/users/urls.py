from django.urls import path

from apps.users.views import (
    IndexView
)
from apps.users.views import register, CustomLoginView, CustomLogoutView



urlpatterns = [
   path('', IndexView.as_view(), name='index'),
    path('account/register/', register, name='register'),
    path('account/login/', CustomLoginView.as_view(), name='login'),
    path('account/logout/', CustomLogoutView.as_view(), name='logout'),
]