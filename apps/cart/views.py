from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Cart, Item, Favorite, Medicine
from apps.cart.forms import AddToFavoriteForm,AddToCartForm

from django.http import JsonResponse


class CartListView(LoginRequiredMixin, TemplateView):
    template_name = 'shopping-cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context['cart'] = cart
        return context

class MinusQuantityView(LoginRequiredMixin, View):
    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        if item.quantity - 1 == 0:
            item.delete()
        else:
            item.quantity -= 1
            item.save()
        return redirect('cart')

class PlusQuantityView(LoginRequiredMixin, View):
    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        item.quantity += 1
        item.save()
        return redirect('cart')

    
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Medicine, id=product_id)
        quantity = int(request.POST.get('quantity', 1))  
        cart, created = Cart.objects.get_or_create(user=request.user)
        

        existing_item = Item.objects.filter(product=product, cart=cart).first()
        if existing_item:
            existing_item.quantity += quantity
            existing_item.save()
        else:
            new_item = Item.objects.create(product=product, cart=cart, quantity=quantity)
        
        return redirect('cart')  
    

class RemoveFromCartView(View):
    def post(self, request, pk):
        item = get_object_or_404(Item, id=pk)
        item.delete()
        return redirect('cart')
    



def apply_coupon(request):
    if request.method == 'POST':
        coupon_code = request.POST.get('coupon_code')

        if coupon_code == 'SUMMER2024':
            request.session['coupon_applied'] = True
            messages.success(request, 'Купон успешно применен.')
        else:
            messages.error(request, 'Неверный код купона.')
    return redirect('checkout')  

def calculate_shipping(request):
    if request.method == 'POST':

        zip_code = request.POST.get('zip_code')
        country = request.POST.get('country')


        if not zip_code:

            return render(request, 'shopping/shopping.html', {'error_message': 'Zip code is required.'})


        try:

            shipping_cost = calculate_shipping_cost(zip_code, country)
            return render(request, 'shopping/shopping.html', {'shipping_cost': shipping_cost})
        except Exception as e:

            return render(request, 'shopping/shopping.html', {'error_message': str(e)})

    return render(request, 'shopping/shopping.html')

def calculate_shipping_cost(zip_code, country):


    if country == 'United Kingdom (UK)':
        return 10.0  
    elif country == 'United States (USA)':
        return 20.0  
    else:
        raise ValueError('Shipping cost calculation not implemented for this country.')


def checkout(request):

    context = {}

    coupon_applied = request.session.get('coupon_applied', False)
    shipping_cost = request.session.get('shipping_cost', 0)
    

    
    context['coupon_applied'] = coupon_applied
    context['shipping_cost'] = shipping_cost
    
    return render(request, 'checkout.html', context)




def update_cart(request):
    if request.method == 'POST':

        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        
      
        return JsonResponse({'message': 'Cart updated successfully'}, status=200)
    else:

        return render(request, 'shopping-cart.html')