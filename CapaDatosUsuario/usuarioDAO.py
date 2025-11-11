from logger_base import log
from cursor_pool import  CursorDelpool
from usuario import Usuario

class UsuarioDao:
    _SELECCIONAR = 'SELECT * FROM "usuario" ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO "usuario"(username,password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE "usuario" SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR= 'DELETE FROM "usuario" WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        try:
            with CursorDelpool() as cursor:
                cursor.execute(cls._SELECCIONAR)
                registros = cursor.fetchall()
                usuario = [Usuario(*registro) for registro in registros]
                for usuarios in usuario:
                    log.debug(usuarios)
                return usuario


        except Exception as e:
            log.error(f'Ocurrió un error al listar los usuarios {e}')

    @classmethod
    def insertar(cls, usuario):
        try:
            with CursorDelpool() as cursor:
                log.debug(f'Usuario insertado: {usuario}')
                valores = (usuario.username, usuario.password)
                cursor.execute(cls._INSERTAR,valores)
                return cursor.rowcount

        except Exception as e:
            log.error(f'Ocurrió un error al insertar los datos{e}')
            return 0


    @classmethod
    def actualizar(cls,usuario):
        try:
            with CursorDelpool() as cursor:
                log.debug(f'Usuario actualizado: {usuario}')
                valores = (usuario.username,usuario.password,usuario.id_usuario)
                cursor.execute(cls._ACTUALIZAR,valores)
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrió un error al actualizar los datos {e}')
            return 0

    @classmethod
    def eliminar(cls,usuario):
        try:
            with CursorDelpool() as cursor:
                log.debug(f'Usuario eliminado: {usuario}')
                valores =(usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR,valores)
                return cursor.rowcount
        except Exception as e:
            log.error(f'Ocurrió un error al eliminar los datos {e}')
            return 0







