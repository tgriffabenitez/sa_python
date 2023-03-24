# Ingresar por consola número de mes e imprimir el nombre de mes correspondiente
# (Ejemplo: 2 -> Febrero). Si es un número no válido mostrar un mensaje de error.
# Resolverlo utilizando una lista.

lista_meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octuble", "noviembre", "diciembre"]
mes_ingresado = int(input("Ingrese el numero de mes: "))

if mes_ingresado < 1 or mes_ingresado > 12:
    print("No existe ese numero de mes")
    
else:
    print(lista_meses[mes_ingresado - 1])