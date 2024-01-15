from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("profesor/list", views.profesor_list, name = "profesor_list" ),
    path("usuario/list", views.usuario_list, name = "usuario_list" ),
    path("clase/list", views.clase_list, name = "clase_list" ),
    path("profesor/create", views.profesor_create, name = "profesor_create" ),
    path("usuarios/create", views.usuario_create, name = "usuario_create" ),
    path("clase/create", views.clase_create, name = "clase_create" ),
   
]



