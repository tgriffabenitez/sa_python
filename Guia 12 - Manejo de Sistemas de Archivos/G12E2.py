# Generar el archivo backup.py, que reciba un directorio como argumento por consola y 
# genere una copia de dicho directorio y su contenido en un directorio para backups 
# c:\bkppy\ creado previamente. La copia del directorio debe contener la fecha en su 
# nombre con formato _aaaammdd.

import os
import sys
import shutil
import time


# Funcion que copia los archivos de un directorio a otro
# recibe como parametro el directorio origen y el directorio destino
def copiar_archivos(directorio, destino):
    for archivo in os.listdir(directorio):
        shutil.copy("{}\\{}".format(directorio, archivo), "{}\\{}".format(destino, archivo))


# Funcion que crea el backup del directorio pasado por parametro
# si no existe el directorio backup, lo crea
# si no existe el directorio destino, lo crea y copia los archivos
# si existe el directorio destino, elimina los archivos y el directorio
# luego, crea nuevamente el directorio y copia los archivos
def crear_backup(directorio):
    fecha = time.strftime("%Y%m%d")
    backup = "c:\\bkppy"
    destino = "{}\\{}_{}".format(backup, directorio, fecha)

    if not os.path.exists(backup):
        os.mkdir(backup)

    # si no existe el directorio destino, lo creo y copio los archivos
    if not os.path.exists(destino):
        os.mkdir(destino)
        copiar_archivos(directorio, destino)

    # si existe el directorio destino, elimino los archivos y el directorio
    # luego, creo nuevamente el directorio y vuelvo a copiar los archivos
    # (esto es para hacer mas de un backup por dia y sobreescribir los archivos)
    else:
        shutil.rmtree(destino)
        os.mkdir(destino)
        copiar_archivos(directorio, destino)


### --- Programa principal --- ###
try:
    directorio = sys.argv[1]
    crear_backup(directorio)

except FileNotFoundError:
    print("El directorio ingresado no existe")

else:
    print("Backup creado con exito")