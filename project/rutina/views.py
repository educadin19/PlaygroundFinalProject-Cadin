from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import EjercicioRutina
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
def index(request):
    return render(request, "rutina/index.html")



class EjercicioRutinaList(ListView):
    model = EjercicioRutina
    template_name = "rutina/ejerciciorutina_list.html"
    context_object_name = "object_list"

 
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')
        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)
            print(queryset.query)  # Imprime la consulta SQL generada
        return queryset


#EjercicioRutina
class EjercicioRutinaCreate(CreateView):
    model = EjercicioRutina
    form_class = EjercicioRutinaForm
    success_url = reverse_lazy ("rutina:ejerciciorutina_list")


class EjercicioRutinaDelete(DeleteView):
    model = EjercicioRutina
    success_url = reverse_lazy ("rutina:ejerciciorutina_list")

class EjercicioRutinaDetail(DetailView):
    model = EjercicioRutina
    

class EjercicioRutinaUpdate(UpdateView):
    model = EjercicioRutina
    form_class = EjercicioRutinaForm
    success_url = reverse_lazy ("rutina:ejerciciorutina_list")

#Ejercicio

class EjercicioList(ListView):
    model = Ejercicio
    template_name = "rutina/ejercicio_list.html"
    context_object_name = "object_list"
    
 
    def get_queryset(self):
        queryset = super().get_queryset()
        consulta = self.request.GET.get('consulta')
        if consulta:
            queryset = queryset.filter(nombre__icontains=consulta)
            print(queryset.query)  # Imprime la consulta SQL generada
        return queryset
    

class EjercicioCreate(CreateView):
    model = Ejercicio
    form_class = EjercicioForm
    success_url = reverse_lazy ("rutina:ejercicio_list")

    

class EjercicioDetail(DetailView):
    model = Ejercicio

class EjercicioDelete(DeleteView):
    model = Ejercicio
    success_url = reverse_lazy ("rutina:ejercicio_list")


class EjercicioUpdate(UpdateView):
    model = Ejercicio
    form_class = EjercicioForm
    success_url = reverse_lazy ("rutina:ejercicio_list")