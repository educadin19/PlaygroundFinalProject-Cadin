from django.contrib import admin
from django.urls import path
from . import views

app_name = "rutina"

urlpatterns = [
    path("", views.index, name="index"),
    #EjercicioRutina
    path("ejerciciorutina/list", views.EjercicioRutinaList.as_view(), name = "ejerciciorutina_list" ),
    path("ejerciciorutina/create", views.EjercicioRutinaCreate.as_view(), name = "ejerciciorutina_create" ),
    path("ejerciciorutina/<int:pk>/update", views.EjercicioRutinaUpdate.as_view(), name = "ejerciciorutina_update" ),
    path("ejerciciorutina/<int:pk>/delete", views.EjercicioRutinaDelete.as_view(), name = "ejerciciorutina_delete" ),
    path("ejerciciorutina/detail/<int:pk>", views.EjercicioRutinaDetail.as_view(), name = "ejerciciorutina_detail" ),
#Ejercicio
    path("ejercicio/list", views.EjercicioList.as_view(), name = "ejercicio_list" ),
    path("ejercicio/create", views.EjercicioCreate.as_view(), name = "ejercicio_create" ),
    path("ejercicio/<int:pk>/update", views.EjercicioUpdate.as_view(), name = "ejercicio_update" ),
    path("ejercicio/<int:pk>/delete", views.EjercicioDelete.as_view(), name = "ejercicio_delete" ),
    path("ejercicio/detail/<int:pk>", views.EjercicioDetail.as_view(), name = "ejercicio_detail" ),
]



