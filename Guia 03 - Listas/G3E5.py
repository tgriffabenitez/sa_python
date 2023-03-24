# Encontrar en una lista de números enteros los divisibles por 10. Ej.
# numeros=[100,5,8,56,99,10]

numeros=[100,5,8,56,99,10]

for numero in numeros:
    if (numero % 10) == 0:
        print(numero)
