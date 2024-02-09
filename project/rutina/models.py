from django.db import models

class EjercicioRutina(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Rutinas"

class Ejercicio(models.Model):
    rutina_id = models.ForeignKey(EjercicioRutina, null=True ,blank=True,on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=100)
    repeticiones = models.IntegerField()
    duracion = models.IntegerField()
    series = models.IntegerField()
    descanso = models.IntegerField()

    def __str__(self):
        return f"{self.rutina_id} - {self.nombre} - {self.duracion} (minutos)"
    class Meta:
        verbose_name ="Ejercicio"
        verbose_name_plural = "Ejercicios"