from logger_base import  log
from conexion import  Conexion

class CursorDelpool:
    def __init__(self):
        self._conn = None
        self._cursor = None

    def __enter__(self):
        self._conn = Conexion.obtenerconexion()
        self._cursor = self._conn.cursor()
        return  self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_val:
            self._conn.rollback()
            log.error('Ocurrio un error no se pueden almacenar los datos')
        else:
            self._conn.commit()
        self._cursor.close()
        Conexion.liberarconexion(self._conn)
