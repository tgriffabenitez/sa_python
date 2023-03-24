# Desarrollar un script para Imprimir todos los argumentos pasados por consola excepto
# el primero correspondiente al nombre del archivo.

import sys

try:
    argumentos = sys.argv[1]
except IndexError:
    print("Error, no hay argumentos.")
else:
    print(sys.argv[1:])