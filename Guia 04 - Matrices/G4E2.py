# Declarar una matriz de 3x3, donde los valores de cada lista serán ceros y sólo un uno en
# cualquier posición.
# Solicitar al usuario una posición de la matriz determinada por fila y columna. Mostrar un
# mensaje de acierto o fallo y solicitar un nuevo ingreso hasta que se acierte la posición
# donde está el uno.

matriz = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

while True:
    fila_ingresada = int(input("Ingrese la fila: "))
    columna_ingresada = int(input("Ingrese la columna: "))

    if matriz[fila_ingresada - 1][columna_ingresada - 1] == 1:
        print("Ganaste")
        break
    else:
        print("Intente nuevamente")
        print()