from django import forms
from . import models


class UsuarioForm(forms.ModelForm):
    class Meta:
            model = models.Usuario
            fields = "__all__"

class ProfesorForm(forms.ModelForm):
    class Meta:
            model = models.Profesor
            fields = "__all__"

class ClaseForm(forms.ModelForm):
    class Meta:
            model = models.Clase
            fields = "__all__"
