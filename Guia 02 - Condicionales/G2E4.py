# Solicitar una edad por consola indicar si la persona es mayor de edad (18 años). Si
# además tiene más de 65 años, mostrar por consola que puede contar con la jubilación

edad = int(input("Ingrese su edad: "))

if edad >= 18 and edad < 65:
    print("Es mayor de edad")

elif edad >= 65:
    print("Puede jubilarse")

else:
    print("Es menor de edad")
