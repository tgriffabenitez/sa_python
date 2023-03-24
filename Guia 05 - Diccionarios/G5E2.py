# Crea un diccionario con los nombres y stock en kilos de distintos metales. Realizar un
# programa que pida el nombre del metal y los kilos que se desean vender del mismo y nos muestre
# si hay o no disponibilidad. Tras cada consulta el programa debe preguntar si queremos hacer otra
# consulta.

diccionario = {"aluminio": 1000, "mercurio": 500, "hierro": 4000, "titanio": 3000}

while True:
	nombre_metal = input("Ingrese el nombre del metal: ")
	kilos_metal = int(input("Ingrese los kilos a comprar: "))
    
	if nombre_metal in diccionario and kilos_metal <= diccionario[nombre_metal]:
		print("Tenemos diponibilidad")

	else:
		print("No tenemos disponibilidad")
	
	if input("Realizar otra consulta? s/n: ") == "n":
		break
