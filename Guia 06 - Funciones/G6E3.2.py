# Solicitar a un usuario una muestra de cinco valores numéricos flotantes, guardarlos en
# una lista y luego calcular el promedio de los mismos a partir de los datos guardados.

def calcular_promedio(lista_numeros):
    total = 0
    for numero in lista_numeros:
        total += numero

    return total / len(lista_numeros)


num_list = []
for i in range(5):
    num = float(input("Ingrese un numero: "))
    num_list.append(num)

promedio = calcular_promedio(num_list)
print("Promedio:", promedio)