# Realizar una función día_x_número que retorne el nombre de un día correspondiente al
# número pasado, detectando los errores en los datos.
def dia_x_numero(numero):
    dias = {1:"Lunes", 2:"Martes", 3:"Miercoles", 4:"Jueves", 5:"Viernes", 6:"Sabado", 7:"Domingo"}

    try:
        dia = dias[numero]
    except KeyError:
        dia = "Numero invalido."
    
    return dia

try:
    numero_dia = int(input("Ingrese el numero: "))
except ValueError:
    print("Debe ingresar un numero entero.")
else:
    print(dia_x_numero(numero_dia))
