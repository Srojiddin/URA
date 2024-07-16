from django.urls import path
from .views import MedicineListView, MedicineCreateView, MedicineSingleListView, MedicineDetailView, MedicineUpdateView, MedicineDeleteView
from . import views

urlpatterns = [
    path('shop/', MedicineListView.as_view(), name='shop'),
    path('medicine/create/', MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/update/<int:pk>/', MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/delete/<int:pk>/', MedicineDeleteView.as_view(), name='medicine_delete'),
    path('product/<int:pk>/', MedicineSingleListView.as_view(), name='product-single'),
    path('medicine/<int:pk>/', views.MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicine/', MedicineListView.as_view(), name='medicine_list'),
]