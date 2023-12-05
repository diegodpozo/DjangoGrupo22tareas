from django.db import models

# Create your models here.
class Reserva(models.Model):
    titulo = models.CharField (max_length=100, verbose_name='titulo')
    descripcion = models.CharField (max_length=100, verbose_name='descripcion')
    fecha_inicio = models.DateField (verbose_name='Fecha de Inicio')
    fecha_fin = models.DateField (verbose_name='Fecha de Fin')

    def __str__(self):
        return f"{'usuario', self.titulo} -- {'categoria', self.descripcion}"