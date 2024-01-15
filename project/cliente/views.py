from django.shortcuts import render, redirect
from .models import Profesor, Usuario, Clase
from . import forms
# Create your views here.


def index(request):
    return render(request, "cliente/index.html")

def profesor_list(request):
    profesores = Profesor.objects.all()
    context =  {"profesores": profesores} 
    return render(request, "cliente/profesor_list.html", context)

def usuario_list(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "cliente/usuario_list.html", context )

def clase_list(request):
    clases = Clase.objects.all()
    context = {"clases": clases}
    return render(request, "cliente/clase_list.html", context )

def usuario_create(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:usuario_list")
    else: #request.method =="GET
        form = forms.UsuarioForm()  
    return render(request, "cliente/usuario_create.html",{"form": form})  

def profesor_create(request):
    if request.method == "POST":
        form = forms.ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:profesor_list")
    else: #request.method =="GET
        form = forms.UsuarioForm()  
    return render(request, "cliente/profesor_create.html",{"form": form})  

def clase_create(request):
    if request.method == "POST":
        form = forms.ClaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:clase_list")
    else: #request.method =="GET
        form = forms.ClaseForm()  
    return render(request, "cliente/clase_create.html",{"form": form})  
        