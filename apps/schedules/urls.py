from django.urls import path

from .views import ScheduleListView
# from .views import schedule_view


urlpatterns = [
    path('time/table/', ScheduleListView.as_view(), name='time_table'),
    # path('schedule/', schedule_view, name='schedule'),
]
