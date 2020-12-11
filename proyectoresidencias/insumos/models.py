from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=300, blank=False, default='')

class Articulo(models.Model):
    familiaId = models.ForeignKey('Familia', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=300, blank=False, default='')
    unidad = models.CharField(max_length=100, blank=False, default='')
    tipo = models.CharField(max_length=50, blank=False, default='')
    grupo = models.CharField(max_length=100, blank=False, default='')
    serie = models.CharField(max_length=300, blank=False, default='')
    parte = models.CharField(max_length=150, blank=False, default='')
    precio = models.CharField(max_length=100, blank=False, default='')
    toxico = models.CharField(max_length=100, blank=False, default='')
    activo =models.BooleanField(default=False)

class Movimiento(models.Model):
    articuloId = models.ForeignKey('Articulo', on_delete=models.CASCADE)
    fecha =  models.DateTimeField(auto_now=True)
    tipo = models.CharField(max_length=50, blank=False, default='')
    cantidad = models.IntegerField(default='0')
    importe = models.CharField(max_length=100, blank=False, default='')
    aplicacion = models.CharField(max_length=100, blank=False, default='')
    referencia = models.CharField(max_length=500, blank=False, default='')
