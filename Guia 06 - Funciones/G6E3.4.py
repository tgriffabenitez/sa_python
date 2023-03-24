# Calcular la cantidad de elemento que tiene una lista (sin utilizar len()).

def lista_len(lista_num):
    total = 0
    for i in lista_num:
        total += 1
    return total


num_list = [-1, 1, 7, 1000, 90, 9]
print(lista_len(num_list))
