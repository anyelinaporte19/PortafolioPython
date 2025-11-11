from django.contrib import admin

from empleados.models import Departamento, Empleado

# Register your models here.

admin.site.register(Departamento)
admin.site.register(Empleado)