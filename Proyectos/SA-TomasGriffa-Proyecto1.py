# Módulo: SA-Proyecto-python.py
# Autor: Tomas Martin, Griffa Benitez
# Correo electrónico: tgriffabenitez@gmail.com
# Fecha: 14-Mar-23
# Descripcion: Entrega del proyecto de python propuesto en clase el dia 14-Mar-23.


productos = []

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
        # arregle la lista producto. Antes tenia una matriz; producto=[[], []]
        producto = []

        nombre_producto = input(">> Ingrese el nombre del producto: ")
        # arregle el texto del input, antes decia "ingrese el nombre del producto"
        precio_producto = float(input(">> Ingrese el precio del producto: "))

        if precio_producto < 0:
            print(">> ERROR: No se puede ingresar un precio menor a 0.")
            print(">> Se cancelo la operacion\n")

        else:
            producto.append(nombre_producto)
            producto.append(precio_producto)
            productos.append(producto)
            print(">> Producto agregado!\n")

    elif opcion == 2:
        print(">> Productos: ")
        for producto in productos:
            print(">> ", producto)
        print()

        producto_a_modificar = int(input(">> Ingrese la fila del producto a modificar (1, 2, 3, ...): "))
        # agregue la validacion para que no se pueda ingresar una fila superior al numero de productos
        while producto_a_modificar > len(productos) or producto_a_modificar < 1:
            print(">> ERROR: No existe ese producto.")
            producto_a_modificar = int(input(">> Ingrese la fila del producto a modificar (1, 2, 3, ...): "))

        nuevo_precio = float(input(">> Ingrese el nuevo precio: "))
        if nuevo_precio < 0:
            print(">> ERROR: verifique los datos ingresados.")
            print(">> Se cancelo la operacion\n")

        else:
            productos[producto_a_modificar - 1][1] = nuevo_precio
            print(">> Precio modificado")
            print(">> El nuevo precio de " + str(productos[producto_a_modificar - 1][0] + " es: " + str(productos[producto_a_modificar - 1][1])))
            print()

    elif opcion == 3:
        print(">> Listado de productos:")
        for producto in productos:
            print(producto)
        print()

    elif opcion == 4:
        print(">> Salio del programa.")
        break

    else:
        print(">> Operacion no valida.")