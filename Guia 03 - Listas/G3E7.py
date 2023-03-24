# Encontrar si un elemento se encuentra en la lista e imprimir la primera posición en que
# aparece.

lista = [1, 3, 1, 2, 3, 9]

buscar_numero = int(input("Ingrese el numero a buscar: "))

for i in range(len(lista)):
    if lista[i] == buscar_numero:
        print("Posicion:", i)
        break

else:
    print("no se encontro")