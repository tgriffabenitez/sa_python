# A partir de una lista de números calcular la suma de sus elementos. (sin utilizar sum())

def sumar_lista(lista_numeros):
    total = 0
    for index in lista_numeros:
        total += index
    return total

num_list = [1, 1, 1, 1, 1]
print(sumar_lista(num_list))