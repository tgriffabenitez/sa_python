# ¿Cuál es el menor número de una lista de números cualquiera?(sin utilizar min())

numeros = [6, 3, -7, 1, 6, 2, 9]
numero_minimo = numeros[0]

for numero in numeros:
    if numero < numero_minimo:
        numero_minimo = numero

print(numero_minimo)