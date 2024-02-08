from django import forms

from .models import *

class EjercicioRutinaForm(forms.ModelForm):
    class Meta:
        model = EjercicioRutina
        fields = "__all__"



class EjercicioForm(forms.ModelForm):
    class Meta:
        model = Ejercicio
        fields = "__all__"