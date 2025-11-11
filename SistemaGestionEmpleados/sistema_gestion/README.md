# Sistema de Gestión de Empleados

Proyecto desarrollado con **Django**, que permite gestionar empleados y departamentos desde una interfaz web.  
Incluye operaciones **CRUD completas** (crear, listar, editar y eliminar empleados), así como **búsqueda filtrada** por nombre y departamento.

---

## Características principales

- CRUD completo de empleados:
  - Agregar nuevos empleados  
  - Listar todos los empleados  
  - Editar información existente  
  - Eliminar empleados
    
- Búsqueda avanzada por:
  - Nombre de empleado  
  - Departamento
- Relación entre modelos:  
  Cada empleado pertenece a un departamento.
- Interfaz web desarrollada con **Django Templates**.
- Validación y manejo de errores con `get_object_or_404`.

---


---

## Tecnologías utilizadas

- **Python**
- **Django**
- **Postgresql** 
- **HTML + Bootstrap (templates)**

---

Instalar dependencias:
python -m pip install django
python -m pip install psycopg2

Crear la base de datos y aplicar migraciones:
python manage.py makemigrations
python manage.py migrate

Crear un superusuario (opcional)
python manage.py createsuperuser

Ejecutar el servidor
python manage.py runserver







