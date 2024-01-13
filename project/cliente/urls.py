from django.contrib import admin
from django.urls import path, include
from . import views



urlpatterns = [
    path("", views.index, name="index"),
    path("profesores", views.profesores_list, name = "profesores" ),
    path("usuarios", views.usuarios_list, name = "usuarios" ),
    path("clases", views.clases_list, name = "clases" ),
    path("Nuevo usuario", views.nuevo_usuario, name = "nuevo_usuario" )
]



