from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from apps.products.models import  Medicine
from apps.cart.models import Cart
from django.views import View
from apps.doctors.forms import DoctorSearchForm


from apps.blogs.forms import BlogSearchForm
from apps.products.forms import MedicineSearchForm


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




from django.shortcuts import render


class MedicineSearchView(View):
    def get(self, request):
        form = MedicineSearchForm()
        return render(request, 'medicine/medicine_search.html', {'form': form, 'medicines': None})

    def post(self, request):
        form = MedicineSearchForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            price_min = form.cleaned_data.get('price_min')
            price_max = form.cleaned_data.get('price_max')

            medicines = Medicine.objects.all()

            if title:
                medicines = medicines.filter(title__icontains=title)

            if price_min is not None:
                medicines = medicines.filter(price__gte=price_min)

            if price_max is not None:
                medicines = medicines.filter(price__lte=price_max)

            return render(request, 'medicine/medicine_search.html', {'form': form, 'medicines': medicines})

        return render(request, 'medicine/medicine_search.html', {'form': form, 'medicines': None})











class SearchView(View):
    def get(self, request):
        # Инициализация форм
        doctor_form = DoctorSearchForm()
        blog_form = BlogSearchForm()
        medicine_form = MedicineSearchForm()

        # Инициализация пустых списков для результатов
        doctors = None
        blogs = None
        medicines = None

        return render(request, 'base/search.html', {
            'doctor_form': doctor_form,
            'blog_form': blog_form,
            'medicine_form': medicine_form,
            'doctors': doctors,
            'blogs': blogs,
            'medicines': medicines,
        })

    def post(self, request):
        # Обработка поиска для каждой формы
        doctor_form = DoctorSearchForm(request.POST)
        blog_form = BlogSearchForm(request.POST)
        medicine_form = MedicineSearchForm(request.POST)

        doctors = None
        blogs = None
        medicines = None

        if doctor_form.is_valid():
            name = doctor_form.cleaned_data.get('name')
            specialization = doctor_form.cleaned_data.get('specialization')

            doctors = Doctor.objects.all()

            if name:
                doctors = doctors.filter(name__icontains=name)
            if specialization:
                doctors = doctors.filter(choosing_a_specialization=specialization)

        if blog_form.is_valid():
            title = blog_form.cleaned_data.get('title')

            blogs = Blog.objects.all()

            if title:
                blogs = blogs.filter(title__icontains=title)

        if medicine_form.is_valid():
            title = medicine_form.cleaned_data.get('title')
            price_min = medicine_form.cleaned_data.get('price_min')
            price_max = medicine_form.cleaned_data.get('price_max')

            medicines = Medicine.objects.all()

            if title:
                medicines = medicines.filter(title__icontains=title)
            if price_min is not None:
                medicines = medicines.filter(price__gte=price_min)
            if price_max is not None:
                medicines = medicines.filter(price__lte=price_max)

        return render(request, 'search.html', {
            'doctor_form': doctor_form,
            'blog_form': blog_form,
            'medicine_form': medicine_form,
            'doctors': doctors,
            'blogs': blogs,
            'medicines': medicines,
        })