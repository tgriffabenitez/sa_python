# Realizar una función divisible_por_5 que si retorne un es divisible por 5 o no y que lance la
# excepción correspondiente si el numero en el argumento no es un entero

def divisible_por_5(num):
    es_divisible = False

    if type(num) != int:
        raise TypeError("El numero ingresado no es un entero.\n")

    if num % 5 == 0:
        es_divisible = True
    return es_divisible

try:
    numero = int(input("Ingrese un numero: "))
except ValueError:
    print("Debe ingresar un numero entero positivo.\n")
else:
    if divisible_por_5(numero):
        print("El numero {} es divisible por 5".format(numero))
    else:
        print("El numero {} no es divisible por 5".format(numero))