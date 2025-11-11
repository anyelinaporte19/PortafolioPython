import logging as log

log.basicConfig(level=log.DEBUG,
                format= '%(asctime)s:%(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                datefmt= '%I:%M:%S %p',
                handlers=[
                    log.FileHandler('capadatos.log')
                ])


if __name__ == '__main__':
    log.debug('Este es un mensaje de tipo debug')
    log.info('Este es un mensaje de tipo info')
    log.warning('Este es un mensaje de tipo warning')
    log.error('Este es un mensaje de tipo error')
