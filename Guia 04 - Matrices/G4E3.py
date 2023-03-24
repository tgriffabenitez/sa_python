# Crear un programa que permita cargar una matriz de dimensiones elegidas por el usuario.
# El código deberá solicitar los números enteros correspondientes a cada celda.
# Supongamos que el usuario elige una matriz de 2 x3
# La entrada y salida del programa para este ejemplo sería similar a la siguiente:

filas = int(input("Ingrese la cantidad de filas: "))
columnas = int(input("Ingrese la cantidad de columnas: "))
matriz = []

for fila in range(filas):
    matriz.append([])
    for columna in range(columnas):
        msg = ("Ingrese el valor de la coordenada ["+ str(fila) + "]["+ str(columna) + "]: ")
        valor = int(input(msg))
        matriz[fila].append(valor)

print("La matriz ingresada es: ", matriz)