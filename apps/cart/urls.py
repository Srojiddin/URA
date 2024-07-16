from django.urls import path
from .views import (
    CartListView,
    MinusQuantityView,
    PlusQuantityView,
    AddToCartView,
    RemoveFromCartView,
)
from . import views

urlpatterns = [
    path('cart/', CartListView.as_view(), name='cart'),
    path('minus/<int:pk>/', MinusQuantityView.as_view(), name='minus_quantity'),
    path('plus/<int:pk>/', PlusQuantityView.as_view(), name='plus_quantity'),
    path('product/<int:product_id>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('cart/<int:pk>/remove/', RemoveFromCartView.as_view(), name='remove_from_cart'),
    path('product/<int:product_id>/add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('apply-coupon/', views.apply_coupon, name='apply_coupon'),
    path('calculate-shipping/', views.calculate_shipping, name='calculate_shipping'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-cart/', views.update_cart, name='update_cart'),

]