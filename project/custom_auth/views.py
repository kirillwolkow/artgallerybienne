from .forms import CustomUserCreationForm, CustomerUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView


class SignupView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class LoginView(LoginView):
    form_class = CustomerUserChangeForm
    sucess_url = reverse_lazy("/")
    template_name = "registration/login.html"
