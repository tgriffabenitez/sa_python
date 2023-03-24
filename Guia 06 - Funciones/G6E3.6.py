# ¿Cuál es el mayor número de una lista de números cualquiera?(sin utilizar max())

def getMax(lista_numeros):
    maximo = lista_numeros[0]
    for numero in lista_numeros:
        if maximo < numero:
            maximo = numero
    return maximo

numeros = [6, 3, -7, 1, 30, 2, -9]
print(getMax(numeros))