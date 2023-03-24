# Generar una función que dado un número retorne su factorial.

def obtener_factorial(numero):
    factorial = 1

    if numero < 0:
        factorial = -1
    
    if (numero == 0) or (numero == 1):
        factorial = 1
    
    while numero > 1:
        factorial *= numero
        numero -= 1

    return factorial


for index in range(1, 7):
    print("El factorial de", index, "es " + str(obtener_factorial(index)))