from django.db import models
from django.contrib.auth.models import User

class Members(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    email = models.CharField(max_length=255, default="N/A")
    image = models.CharField(max_length=255, blank=True)
    cvlac = models.CharField(max_length=255, default="N/A")

    def __str__(self):
        return self.name

class Novelty(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.description

class Publications(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    date = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class RegisterWeek(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.date

class RegisterMicroinverser(models.Model):
    modelo = models.CharField(max_length=100, default="N/A")
    ubicacion = models.CharField(max_length=100, default="")
    puerto = models.IntegerField()
    direccion_ip = models.CharField(max_length=100, default="")
    capacidad_panel = models.IntegerField()
    rendimiento_energetico = models.FloatField()
    usuario = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.ubicacion

class Materials(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    actualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class BaseData(models.Model):
    voltaje_entrada = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    voltaje_salida = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    corriente_entrada = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    corriente_salida = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    potencia_entrada = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    potencia_salida = models.DecimalField(max_digits=10, decimal_places=5, default=0)
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.fecha)

class DataMicroinverser(BaseData):
    microinversor = models.ForeignKey(RegisterMicroinverser, on_delete=models.CASCADE)
    pass
