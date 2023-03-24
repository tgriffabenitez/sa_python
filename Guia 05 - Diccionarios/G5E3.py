# Escribe un programa que pida un número por consola y que cree un diccionario cuyas claves
# sean desde el número 1 hasta el número indicado incluido, y los valores sean los cuadrados de las
# claves.

numero_ingresado = int(input("Ingrese un numero: "))

diccionario = {}

for numero in range(1, numero_ingresado + 1):
    diccionario[numero] = numero**2

print("numero -> cuadrado")
for item in diccionario:
    print(f"{item} -> {diccionario[item]}")