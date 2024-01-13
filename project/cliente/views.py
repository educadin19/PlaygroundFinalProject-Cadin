from django.shortcuts import render
from .models import Profesor, Usuario, Clase
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