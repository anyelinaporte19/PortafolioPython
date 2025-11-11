from logger_base import log
from psycopg2 import  pool
import  sys

class Conexion:
    _DATABASE = 'users_db'
    _USERNAME = 'postgres'
    _PASSWORD = 'admin'
    _DB_PORT = '5432'
    _HOST = '127.0.0.1'
    _MIN_CON = 1
    _MAX_CON = 5
    _pool = None

    @classmethod
    def obtenerpool(cls):
        if cls._pool is None:
            try:
                cls._pool = pool.SimpleConnectionPool(cls._MIN_CON, cls._MAX_CON,
                                                      user= cls._USERNAME,
                                                      password = cls._PASSWORD,
                                                      host= cls._HOST,
                                                      port=cls._DB_PORT,
                                                      database= cls._DATABASE,
                                                      options= '-c client_encoding=UTF8')
                return cls._pool
            except Exception as e:
                log.error(f'Ocurrió un error {e}')
                sys.exit()
        else:
            return cls._pool

    @classmethod
    def obtenerconexion(cls):
        try:
            conexion = cls.obtenerpool().getconn()
            return conexion
        except Exception as e:
            log.error(f'Ocurrio un error de conexión: {e}')
            sys.exit()

    @classmethod
    def liberarconexion(cls, conexion):
        try:
            cls.obtenerpool().putconn(conexion)
        except Exception as e:
            log.error(f'Ocurrió un error {e}')

    @classmethod
    def cerrarconexion(cls):
        try:
            cls.obtenerpool().closeall()

        except Exception as e:
            log.error(f'Ocurrió un error al cerrar la conexión {e} ')

