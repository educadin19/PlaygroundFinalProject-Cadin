from django.shortcuts import render
from .models import Profesor
# Create your views here.


def index(request):
    profesores = Profesor.objects.all()
    
    return render(request, "cliente/index.html", {"profesores": profesores})

