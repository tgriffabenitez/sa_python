# Generar una función que renorne si un número es par o no , para poder llamarla luego desde
# un programa principal.

def esPar(numero):
    if (numero & 1):
        return False
    return True


for index in range(1, 21):
    if esPar(index):
        print("El numero " + str(index) + " es par")
    else:
        print("El numero " + str(index) + " es impar")