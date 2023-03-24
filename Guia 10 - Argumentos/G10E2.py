# Desarrollar un script buscar_archivos.py que reciba como argumentos la ruta a un
# directorio y un nombre de archivo, o parte de él. Deberá buscar los archivos dentro del 
# directorio que concuerden con el segundo argumento ingresado y listarlos.
# Si no se pasan los argumentos o la ruta especificada no existe, el programa debe mostrar 
# el error en la consola y concluir.

import os
import sys

try:
    ruta = sys.argv[1]
    nombre_archivo = sys.argv[2]
    
    total_archivos = os.listdir(ruta)
    for archivo in total_archivos:
        if archivo.startswith(nombre_archivo):
            print(archivo)

except IndexError:
    print("Error, no se ingresaron los argumentos.")

except FileNotFoundError:
    print("No existe el archivo")