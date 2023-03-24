# Escribe un programa que cree un diccionario simulando un ticket de una compra. El programa
# debe preguntar el artículo y su precio, y añadir el par al diccionario, hasta que el usuario decida
# terminar. Después se debe mostrar por pantalla la lista de la compra y el costo total

diccionario = {}
lista = []
total = 0

while True:
    articulo = input("Ingrese el articulo: ")
    precio = float(input("Ingrese el precio: "))
    diccionario[articulo] = precio
    total =+ precio
    
    if input(("Desea terminar? s/n: ")) == "s":
        print()
        break

print("{:<15} {:>10}".format("Articulo", "Precio"))
for item in diccionario:
    print("{:<15} {:>10.2f}".format(item, diccionario[item]))

print("----------------------------")
print("{:<15} {:>10.2f}".format("Total", total))
