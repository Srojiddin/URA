from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.products.models import  Medicine
from apps.cart.models import Cart



from .forms import MedicineCreateForm,MedicineUpdateForm,MedicineDeleteForm
from apps.cart.forms import AddToCartForm

class MedicineDeleteView(generic.DeleteView):
    model = Medicine
    template_name = 'medicine/medicine_delete.html'
    success_url = reverse_lazy('shop')  






class MedicineUpdateView(generic.CreateView):
    model = Medicine
    form_class = MedicineUpdateForm
    template_name = 'medicine/medicine_update.html'
    success_url = reverse_lazy('shop')
    context_object_name = "products"




class MedicineCreateView(generic.CreateView):
    model = Medicine
    form_class = MedicineCreateForm
    template_name = 'medicine/medicine_create.html'
    success_url = reverse_lazy('shop')
    context_object_name = "products"

class MedicineDetailView(generic.DetailView):
    model = Medicine
    template_name = 'shop-single.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        context['form'] = AddToCartForm(initial={'product': product, 'cart': cart})
        return context

class MedicineListView(generic.ListView):
    model = Medicine
    template_name = 'shop.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        product_forms = []
        for product in context['products']:
            form = AddToCartForm(initial={'product': product, 'cart': cart})
            product_forms.append((product, form))
        context['product_forms'] = product_forms
        return context

# class MedicineSingleListView(generic.ListView):
#     model = Medicine
#     template_name = 'shop-single.html'
#     context_object_name = 'products'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         cart, created = Cart.objects.get_or_create(user=self.request.user)
#         product_forms = []
#         for product in context['products']:
#             form = AddToCartForm(product=product, cart=cart)
#             product_forms.append((product, form))
#         context['product_forms'] = product_forms
#         return context

class MedicineSingleListView(generic.DetailView):
    model = Medicine  # Указываем модель, с которой работаем
    template_name = 'shop-single.html'  # Шаблон для отображения деталей
    context_object_name = 'medicine'  # Имя переменной контекста, которая будет содержать объект Medicine

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddToCartForm()  # Добавляем форму для добавления в корзину
        return context