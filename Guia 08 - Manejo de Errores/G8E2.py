# Ingresar dos números e imprimir el resultado de las cuatro operaciones básicas (+, -,* ,/)

def suma(num1, num2):
    if (type(num1) != int and type(num1) != float) or (type(num2) != int and type(num2) != float):
        raise TypeError("Los tipos de datos soportados son int y float")
    return num1 + num2


def resta(num1, num2):
    if (type(num1) != int and type(num1) != float) or (type(num2) != int and type(num2) != float):
        raise TypeError("Los tipos de datos soportados son int y float")
    return num1 - num2


def producto(num1, num2):
    if (type(num1) != int and type(num1) != float) or (type(num2) != int and type(num2) != float):
        raise TypeError("Los tipos de datos soportados son int y float")
    return num1 * num2


def division(num1, num2):
    if (type(num1) != int and type(num1) != float) or (type(num2) != int and type(num2) != float):
        raise TypeError("Los tipos de datos soportados son int y float")
   
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir por cero.\n")
    else:
        return num1 / num2


while True:

    print("|----------------------------------------|")
    print("| 1 - Sumar.                             |")
    print("| 2 - Restar.                            |")
    print("| 3 - Multiplicar.                       |")
    print("| 4 - Dividir.                           |")
    print("| 5 - Salir.                             |")
    print("|----------------------------------------|")
    try:
        opcion = int(input(">> Ingrese la operacion: "))
    except ValueError:
            print("Debe ingresar un numero entero positivo entre 1 y 5.\n")
            continue
    
    if opcion == 1:
        try:
            num1 = int(input("Ingrese un numero: "))
            num2 = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero entero positivo.\n")
        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("El resultado es: {}.\n".format(suma(num1, num2)))

    elif opcion == 2:
        try:
            num1 = int(input("Ingrese un numero: "))
            num2 = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero entero positivo.\n")
        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("El resultado es: {}.\n".format(resta(num1, num2)))

    elif opcion == 3:
        try:
            num1 = int(input("Ingrese un numero: "))
            num2 = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero entero positivo.\n")
        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("El resultado es: {}.\n".format(producto(num1, num2)))

    elif opcion == 4:
        try:
            num1 = int(input("Ingrese un numero: "))
            num2 = int(input("Ingrese un numero: "))
        except ValueError:
            print("Debe ingresar un numero entero positivo.\n")
        except Exception as e:
            print("Error: {}".format(e))
        else:
            print("El resultado es: {}.\n".format(division(num1, num2)))
    
    elif opcion == 5:
        print("Saliendo...\n")
        break

    else:
        print("Debe ingresar un numero entero positivo entre 1 y 5.\n")