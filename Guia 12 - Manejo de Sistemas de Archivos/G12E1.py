# Del drive descargar el programa procesos.exe. El mismo muestra en consola una tabla 
# con el PID, nombre y usuario de cada proceso corriendo en el sistema.
# Crear un script buscar_proceso.py que reciba como argumento a través de la consola el 
# nombre de un proceso, ejecute el programa procesos.exe e imprima su PID y usuario. 
# Si hay varios procesos con el mismo nombre, debe imprimir la información de todos ellos.
# Si el nombre del proceso no se ha pasado, debe mostrar un error en la consola y concluir.
# En los procesos en que no aparezca el usuario reemplazarlo por una cadena vacía.

import subprocess
import sys

# Funcion que imprime la lista de procesos en forma de tabla
def imprimirProcesos(procesos):
    print("{:<10} {:>}".format("PID", "USUARIO"))
    for item in procesos:
        if item[2] == "-":
            print("{:<10} {:>}".format(item[0], " "))
        else:
            print("{:<10} {:>} ".format(item[0], item[2]))


# Funcion que recibe el nombre de un proceso
# Devuelve una lista con los procesos que coinciden con ese nombre
def obtener_procesos(nombre_proceso):
    proceso_path = "procesos.exe"
    procesos = subprocess.run([proceso_path, nombre_proceso], capture_output=True, encoding="cp850")

    # separo el proceso por lineas
    procesos = procesos.stdout.split("\n")
    
    # elimino las primeras 3 lineas y las ultimas 2
    procesos = procesos[3:-2]

    # separo cada linea por el caracter | y despues elimino los espacios en blanco
    output = []
    for linea in procesos:
        proceso = linea.strip("|").split("|")

        # elimino los espacios en blanco de cada elemento de la lista
        for i in range(len(proceso)):
            proceso[i] = proceso[i].strip()

        # si el nombre del proceso coincide con el nombre pasado por parametro lo agrego a la lista
        if proceso[1].lower() == nombre_proceso:
            output.append(proceso)
    
    if len(output) == 0:
        raise Exception("No se encontro el proceso {}".format(nombre_proceso))
    
    return output


try:
    nombre_proceso = sys.argv[1].lower()
    procesos = obtener_procesos(nombre_proceso)
    
except IndexError:
    print("Debe ingresar un proceso a buscar")

except FileNotFoundError:
    print("No se encuentra el programa procesos.exe")

except Exception as e:
    print(e)

else:
    imprimirProcesos(procesos)