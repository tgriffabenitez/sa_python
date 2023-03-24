# Solicitar a un usuario diez números enteros al azar. Una vez finalizado el ingreso, mostrarlos
# ordenados y sin números repetidos

numeros_ingresados = []

for index in range(0, 10):
    numero_ingresado = int(input("Ingrese un numero: "))
    numeros_ingresados.append(numero_ingresado)

numeros_sin_repetidos = list(set(numeros_ingresados))
numeros_ordenados = sorted(numeros_sin_repetidos)

print(numeros_ordenados)
