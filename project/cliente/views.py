from django.shortcuts import render, redirect
from .models import Profesor, Usuario, Clase
from . import forms
# Create your views here.


def index(request):
    return render(request, "cliente/index.html")

def profesores_list(request):
    profesores = Profesor.objects.all()
    context =  {"profesores": profesores} 
    return render(request, "cliente/cliente_profesores.html", context)

def usuarios_list(request):
    usuarios = Usuario.objects.all()
    context = {"usuarios": usuarios}
    return render(request, "cliente/cliente_usuarios.html", context )

def clases_list(request):
    clases = Clase.objects.all()
    context = {"clases": clases}
    return render(request, "cliente/cliente_clases.html", context )

def nuevo_usuario(request):
    if request.method == "POST":
        form = forms.UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("cliente:usuarios_list")
    else: #request.method =="GET
        form = forms.UsuarioForm()  
    return render(request, "cliente/nuevo_usuario.html",{"form": form})  
    