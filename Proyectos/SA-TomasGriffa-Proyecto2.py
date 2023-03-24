# Módulo: SA-TomasGriffa-Proyecto2.py
# Autor: Tomas Martin, Griffa Benitez
# Correo electrónico: tgriffabenitez@gmail.com
# Fecha: 15-Mar-23
# Descripcion: Entrega del proyecto de python propuesto en clase el dia 15-Mar-23.

productos = {}

while True:
    print("|----------------------------------------|")
    print("| 1 - Alta de Producto.                  |")
    print("| 2 - Modificacion de Precio.            |")
    print("| 3 - Listado de Productos.              |")
    print("| 4 - Salir.                             |")
    print("|----------------------------------------|")
    opcion = int(input(">> Ingrese la operacion: "))
    print()

    if opcion == 1:
        intentos = 0 # Agregue un contador para que el programa vuelva al menu principal en caso que el usuario se equivoque consecutivamente
        while True:
            nombre_producto = input("Ingrese el nombre del producto: ")
            if nombre_producto in productos:
                intentos += 1
                if intentos == 3:
                    print("Se agoto el numero de intentos.\n")
                    break
                else:
                    print("El producto ya esta almacenado, actualice su precio.\n")
                    break
            else:
                intentos = 0
                while True:
                    precio_producto = float(input("Ingrese el precio del producto: "))  
                    if precio_producto < 0:
                        intentos += 1
                        if intentos == 3:
                            print("Se agoto el numero de intentos.\n")
                            break
                        else:
                            print("No se puede ingresar un precio menor a 0.\n")
                    else:
                        productos[nombre_producto] = precio_producto
                        break            
            if input("Agregar mas productos? s/n: ") == "n":
                print()
                break

    elif opcion == 2:
        print("{:<15}".format("Productos almacenados:")) # Si bien no vimos en clase el metodo .format() lo implemente en varios lugares para mejorar el output
        for producto in productos:
            print("{:<15}".format(producto))
        print()

        intentos = 0
        while True:
            producto_a_modificar = input("Ingrese el nombre del producto a modificar: ")
            if producto_a_modificar not in productos:
                intentos += 1
                if intentos == 3:
                    print("Se agoto el numero de intentos.\n")
                    break
                else:
                    print("El producto ingresado no esta almacenado.\n")
            else:
                intentos = 0
                while True:
                    nuevo_precio = float(input("Ingrese el nuevo precio: "))
                    if nuevo_precio < 0:
                        intentos += 1
                        if intentos == 3:
                            print("Se agoto el numero de intentos.\n")
                            break
                        else:
                            print("El precio no peude ser negativo.\n")
                    else:
                        productos[producto_a_modificar] = nuevo_precio
                        print("El nuevo precio de {} es {}".format(producto_a_modificar, nuevo_precio))
                        print()
                        break
                break

    elif opcion == 3:
        print("{:<15} {:>10}".format("Producto", "Precio")) # agregue el .format() para que el output se vea en forma de lista
        print("----------------------------")
        for producto in productos:
            print("{:<15} {:>10.2f}".format(producto, productos[producto]))
        print()
        
    elif opcion == 4:
        print("Salio del programa.\n")
        break

    else:
        print("Operacion no valida.\n")