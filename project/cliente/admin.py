from django.contrib import admin

# Register your models here.

from .models import Persona, Profesor, Usuario, Clase


admin.site.register(Profesor)
admin.site.register(Usuario)
admin.site.register(Clase)