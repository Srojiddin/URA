from django.urls import path

from .views import ScheduleListView
# from .views import schedule_view
from .views import ScheduleCreateView, ScheduleDeleteView

urlpatterns = [
    path('time/table/', ScheduleListView.as_view(), name='time_table'),
    # path('schedule/', schedule_view, name='schedule'),
    path('schedule/create/', ScheduleCreateView.as_view(), name='schedule_create'),
    path('schedule/<int:pk>/delete/', ScheduleDeleteView.as_view(), name='schedule_delete'),

]
