# Solicitar a un usuario una muestra de cinco valores numéricos flotantes, guardarlos en
# una lista y luego calcular el promedio de los mismos a partir de los datos guardados.

MAX_NUM = 5
num_list = []

for i in range(MAX_NUM):
    num = float(input("Ingrese un numero: "))
    num_list.append(num)

promedio = sum(num_list)/MAX_NUM
print("Promedio:", promedio)
