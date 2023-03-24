# Generar un reloj en consola que muestre hora, minutos y segundos actualizándose en intervalos
# de un segundo.
# Tips:
# Para limpiar el contenido de la consola podemos utilizar el módulo os de la siguiente forma
# os.system('cls' if os.name == 'nt' else 'clear')
# El método sleep() del módulo time permite generar detener la ejecución del programa en el
# intervalo de segundo colocado como parámetro.

import os
from time import sleep
from datetime import datetime

while True:
    reloj = datetime.today().strftime("%H:%M:%S")
    print(reloj)
    sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')