from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_title = "Rutinas"

class EjercicioRutinaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

class EjercicioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)
    ordering = ('nombre', "rutina_id",)

admin.site.register(EjercicioRutina, EjercicioRutinaAdmin)
admin.site.register(Ejercicio, EjercicioAdmin)