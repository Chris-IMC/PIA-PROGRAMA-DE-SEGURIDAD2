import logging
import hashlib

logging.basicConfig(level=logging.INFO, filemode="Tareas_de_ciberseguridad.log", format="%(asctime)s - %(levelname)s - %(message)s")
'''
logger = logging.getLogger(__name__)

handler = logging.FileHandler('prueba1.log')

logger.info("prueba del logger")
'''

class Hash:

    def menu(self):
        clear()

        Archivo = input("Ingrese el nombre del archivo que desea sacar su valor Hash:")

        while True:
            try:
                with open(Archivo, 'rb') as f:
                    SHA512 = hashlib.sha512()
                    for chunk in iter(lambda: f.read(4096), b""):
                        SHA512.update(chunk)
                        print(SHA512.hexdigest())
                    break
            except Exception as error:
                logging.error(error, exc_info=True)
                print("Error" % datetime.now())



