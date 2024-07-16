from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.db import IntegrityError
from django.contrib.auth.views import LogoutView
from django.contrib.auth import logout
from .forms import CustomAuthenticationForm
from .forms import CustomUserRegisterForm


from apps.doctors.models import Doctor
from django.views.generic import  TemplateView





class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['doctors'] = Doctor.objects.all()

        return context



from .forms import CustomAuthenticationForm
from .forms import CustomUserRegisterForm


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'You have successfully logged out.')
        return redirect('/')


class CustomLoginView(LoginView):
    template_name = 'user/register.html'
    authentication_form = CustomAuthenticationForm

    def form_valid(self, form):
        # This method is called when form is valid
        login(self.request, form.get_user())
        messages.success(self.request, 'Вы успешно вошли в систему.')
        return redirect('/')


def register(request):
    if request.method == 'POST':
        form = CustomUserRegisterForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                login(request, user)
                messages.success(request, 'Регистрация прошла успешно.')
                return redirect('/')
            except IntegrityError:
                form.add_error('username', 'Это имя пользователя уже занято.')
        else:
            messages.error(request, 'Ошибка регистрации. Пожалуйста, исправьте ошибки ниже.')
    else:
        form = CustomUserRegisterForm()

    context = {
        'form': form
    }
    return render(request, 'user/register.html', context)


