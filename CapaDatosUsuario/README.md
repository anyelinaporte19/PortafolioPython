# Sistema de Gestión de Usuarios (Capa de Datos)

Aplicación de consola desarrollada en **Python**, que implementa una **capa de datos con pool de conexiones** para gestionar usuarios en una base de datos.  
Permite **listar, agregar, actualizar y eliminar usuarios** de manera eficiente y estructurada.

---

## Características principales

- Arquitectura por **capas** (Capa de Datos, Capa de Dominio y Capa de Aplicación).
- Uso de **pool de conexiones** para mejorar el rendimiento en operaciones con la base de datos.
- CRUD completo:
  - Listar usuarios
  - Agregar usuario
  - Actualizar usuario
  - Eliminar usuario
- Menú de **consola interactivo** para navegar entre las opciones.
- Código modular, legible y escalable.

---


## Tecnologías utilizadas

- **Python**
- **psycopg2** (para PostgreSQL) 
- **Base de datos relacional**
- **Pycharm**

---

## Requisitos previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior  
- Una base de datos configurada (PostgreSQL o MySQL)
- Las dependencias del proyecto:

python -m pip install psycopg2

## Configuración del entorno

Crea una base de datos llamada users_db (puedes cambiar el nombre si lo ajustas en el código).

En el archivo conexion.py, configura tus credenciales:
### Clase de conexión
```python
class Conexion:
    _DATABASE = 'users_db'
    _USERNAME = 'tu_usuario'
    _PASSWORD = 'tu_contraseña'
    _DB_PORT = '5432'
    _HOST = 'localhost'


## Crea la tabla de usuarios:

CREATE TABLE usuario (
    id_usuario SERIAL PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50)
);





