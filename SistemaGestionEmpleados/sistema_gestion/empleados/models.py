from django.db import models
from django.db.models import SET_NULL


# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.email}'