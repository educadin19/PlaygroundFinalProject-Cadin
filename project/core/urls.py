from django.urls import path, include
from .views import index, about
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from .views import CustomLoginView, register

urlpatterns = [
    path('', index, name="index"),
    path('about', about, name="about"),
    path('', include("cliente.urls"), name="cliente"),
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="core/logout.html"), name="logout"),
    path("register/", register, name="register"),
]


