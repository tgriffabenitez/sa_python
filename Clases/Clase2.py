## Colecciones
# LISTAS: ordenadas modificables
# DICCIONARIOS: no ordenados, modificables
# TUPLAS: ordenadas, no modificables
# SET: no ordenados, no modificables

## listas
lista_uno = [10, 20, 30, 40]
lista_dos = [1, 2.5, True, "Hola"]

# agregar elementos a una lista
lista_uno.append(50)      # ingresa el elemento 50 al final de la lista
lista_uno.insert(2, 60)   # ingresa el elemento 60 en la posicion 2 y desplaza a la derecha el resto


# eliminar elementos de una lista
del lista_uno[3]                         # elimina el elemento que esta en la posicion 3 de la lista
lista_dos.remove("Hola")                 # elimina la primera ocurrencia de ese valor
item_borrado = lista_dos.pop(2)          # elimina el elemnto el la posicion 2 y retora el valor borrado

# obenter la longitud de una lista:
len(lista_uno)
print(len(lista_uno))

# recorrer una lista con ciclo for
for item in lista_uno:
    print(item)

# range(desde, hasta, incremento)
# range(0, 5, 1) >> [0, 1, 2, 3, 4]. El valor hasta no se incluye, siempre es uno menos.
# range(1, 5, 1) >> [1, 2, 3, 4].
# range(5, -1, -1) >> [5, 4, 3, 2, 1, 0]

for item in range(len(lista_uno)):
    print(lista_uno[item])


## Lista de listas
lista_tres = [[1, 2, 3], ["a", "b"], ["c", 8, 9]]

# las listas que son "cuadradas" se las conoce como matrices
matriz_uno = [[10, 20], [30, 40], [50, 60]] # Matrix 3x2

# forma 1 de recorrer una matriz
for fila in range(len(matriz_uno)):
    for columna in range(len(matriz_uno[0])):
        print(matriz_uno[fila][columna])


# forma 2 de recorrer una matriz
for fila in matriz_uno:
    for columna in fila:
        print(matriz_uno[fila][columna])


# cargar una matriz
matriz = []
valor = 0

for fila in range(0, 2, 1):
    matriz.append([])
    print(matriz)
    for columna in range(0, 3, 1):
        valor += 10
        matriz[fila].append(valor)
print(matriz)
