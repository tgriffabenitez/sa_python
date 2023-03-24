# Insertar un número por consola e indicar si el mismo es o no par

num = int(input("Ingrese un numero entero: "))

if (num & 1):
    print("Es impar")
else:
    print("Es par")