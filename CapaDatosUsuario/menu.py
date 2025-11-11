from usuario import  Usuario
from usuarioDAO import UsuarioDao
print('----Sistema de usuarios----')
opcion = 0

while opcion !=5:
    print(f'Lista de opciones:'
          f'\n1.Listar usuarios'
          f'\n2.Agregar usuario'
          f'\n3.Actualizar usuario'
          f'\n4.Eliminar usuario'
          f'\n5.Salir')
    try:
        opcion =int(input('Escribe tu opción(1-5): '))
    except Exception as e:
        print(f'Ingrese una opción válida: {e}')
        opcion = 0
        continue

    if opcion == 1:
        usuario = UsuarioDao.seleccionar()
        for persona in usuario:
            print(persona)
    elif opcion ==2:
        user = input(f'Ingrese el username: ')
        contrasenia = input(f'Ingrese el password: ')
        users = Usuario(username =user, password=contrasenia)
        usuarios_insertados = UsuarioDao.insertar(users)
        print(f'Usuarios insertados: {usuarios_insertados}')

    elif opcion ==3:
        id_user = int(input('Escribe el id_usuario a modificar:'))
        user = input('Escribe el nuevo username: ')
        contrasenia = input('Escribe el nuevo password:')
        usuario = Usuario(id_usuario=id_user, username=user, password=contrasenia)
        usuarios_actualizados = UsuarioDao.actualizar(usuario)
        print(f'Usuarios actualizados: {usuarios_actualizados}')

    elif opcion ==4:
        id_user = int(input('Escribe el id_usuario a eliminar:'))
        usuario = Usuario(id_usuario=id_user,username=None, password=None)
        usuarios_eliminados = UsuarioDao.eliminar(usuario)
        print(f'Usuarios eliminados: {usuarios_eliminados}')
    elif opcion ==5:
        print('Hasta la próxima!')
    else:
        print('Ingrese una opción válida(1-5): ')



