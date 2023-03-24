# Ingresar por consola número de mes e imprimir el nombre de mes correspondiente
# Si es un número no válido mostrar un mensaje de error.
# Resolverlo utilizando una lista.

def obtener_mes(numero_mes):
    lista_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octuble", "noviembre", "diciembre"]

    if mes_ingresado < 1 or mes_ingresado > 12:
        print("No existe ese numero de mes")
    else:
        print(lista_meses[numero_mes - 1])


mes_ingresado = int(input("Ingrese el numero de mes: "))
obtener_mes(mes_ingresado)
