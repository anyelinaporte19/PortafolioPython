"""
URL configuration for sistema_gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from empleados.views import listar_empleados, agregar_empleado, editar_empleado, eliminar_empleado

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_empleados, name='listar_empleados'),
    path('agregar/', agregar_empleado, name='agregar_empleado'),
    path('editar/<int:id>', editar_empleado, name='editar_empleado'),
    path('eliminar<int:id>', eliminar_empleado, name='eliminar_empleado'),

]
