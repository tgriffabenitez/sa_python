# Una medida de la obesidad se determina mediante el índice de masa corporal (IMC),
# que se calcula dividiendo los kilogramos de peso por el cuadrado de la estatura en metros
# (IMC = peso [kg]/ estatura [m2])
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros) y de
# acuerdo a la siguiente tabla calcule el índice de masa corporal, lo almacene en una
# variable, y muestre por pantalla el índice de masa corporal calculado redondeado con dos
# decimales y la composición corporal.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en kg: "))

icm = peso / (altura**2)

if icm < 18.5:
    print("Peso inferior al normal")

elif icm >= 18.5 and icm <= 24.9:
    print("Normal")

elif icm > 24.9 and icm <= 29.9:
    print("Peso superior al normal")

elif icm > 30:
    print("Obesidad")
    
else:
    print("Error en alguno de los datos ingresados")