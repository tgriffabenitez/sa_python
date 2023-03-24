# Encontrar en una lista de números enteros los divisibles por 10. Ej.
# numeros=[100,5,8,56,99,10]

def numeros_divisibles(lista_numeros):
    divisibles = []
    for numero in lista_numeros:
        if (numero % 10) == 0:
            divisibles.append(numero)

    return divisibles

numeros = [100,5,8,56,99,10]
print(numeros_divisibles(numeros))