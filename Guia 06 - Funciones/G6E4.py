# Generar una función que dado un número retorne si el mismo es primo o no.

def esPrimo(numero):
    es_primo = True

    if numero < 2:
        es_primo = False

    for i in range(2, numero):
        if (numero % i) == 0:
            es_primo = False
            break

    return es_primo

for i in range(1, 50):
    if esPrimo(i):
        print("El numero:", i, "es primo")