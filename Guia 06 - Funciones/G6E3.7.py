# Encontrar si un elemento se encuentra en la lista e imprimir la primera posición en que
# aparece.

def buscar_en_lista(numero, lista_numero):
    posicion = 0
    for index in range(len(lista_numero)):
        if numero == lista_numero[index]:
            posicion = index
            break

    return posicion


lista = [1, 3, 1, 2, 3, 9]
buscar_numero = int(input("Ingrese el numero a buscar: "))
print("El numero", buscar_numero, "esta en la posicion", buscar_en_lista(buscar_numero, lista))
