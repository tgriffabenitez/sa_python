# Módulo: SA-TomasGriffa-Proyecto3.py
# Autor: Tomas Martin, Griffa Benitez
# Correo electrónico: tgriffabenitez@gmail.com
# Fecha: 16-Mar-23
# Descripcion: Entrega del proyecto de python propuesto en clase el dia 16-Mar-23.


### OBSERVACIONES ###
# En comparación con la versión anterior, elimine los bloques while True: que utilizaba para validar 
# la entrada de datos, ya que esto complicaba la lectura del código. 
# En cambio, si el usuario ingresa un valor incorrecto, simplemente lo devuelvo al menú principal
# indicando con un mensaje el que error cometio


### FUNCIONES ###

# Funcion que muestra en la consola el menu del programa.
# Devuelve el valor de la seleccion del usuario.
def mostrarMenu():
    print("|----------------------------------------|")
    print("| 1 - Alta de Producto.                  |")
    print("| 2 - Modificacion de Precio.            |")
    print("| 3 - Listado de Productos.              |")
    print("| 4 - Salir.                             |")
    print("|----------------------------------------|")
    opcion = int(input(">> Ingrese la operacion: "))
    return opcion


# Funcion que imprime los productos y precios en forma de tabla
# A comparacion de la version anterior, tambien elimine los < > que
# usaba para darle formato al texto y ponerlos a la derecha e izquierda
# Recibe un diccionario con los productos almacenados
def mostrarProductos(productos):
        print("\n")
        print("{:15} {:10}".format("Producto", "Precio"))
        print("------------------------------")
        for producto in productos:
            print("{:15} {:10.2f}".format(producto, productos[producto]))
        print("\n")


# Funcion que guarda el producto en el diccionario
# Recibe un diccionario con los productos almacenados, el nombre del producto y su precio
def guardarProducto(productos, nombre_producto, precio_producto):
    productos[nombre_producto] = precio_producto


# Como en la version anterior habia utilizado el keyword "in" con un if
# y no lo vimos en clase. Arme una funcion que verifica si existe el producto
# Esta funcion recibe el diccionario de productos y el producto a buscar
def existeProducto(productos, buscar_producto):
    existe = False
    for producto in productos:
        if producto == buscar_producto:
            existe = True
    return existe

# Funcion para validar el precio ingresado por el usuario
# Recibe un float y verifica que sea mayor a 0.
def validarPrecio(precio):
    esValido = False
    if precio > 0:
        esValido = True
    return esValido
        
       
# Funcion que agrega un nuevo producto al diccionario
# Recibe un diccionario con los productos almacenados
def agregarProducto(productos):
    nombre_producto = input("\nIngrese el nombre del producto: ")
    if existeProducto(productos, nombre_producto):
        print("El producto ya esta almacenado, actualice su precio.\n")
    else:
        precio_producto = float(input("Ingrese el precio del producto: "))
        if validarPrecio(precio_producto):
            guardarProducto(productos, nombre_producto, precio_producto)
        else:
            print("No se puede ingresar in precio negativo.\n")       


# Funcion que modifica el precio de un producto almacenado en el diccionario
# Recibe un diccionario con los productos almacenados
def modificarPrecio(productos):
        producto_a_modificar = input("Ingrese el nombre del producto a modificar: ")
        if existeProducto(productos, producto_a_modificar):
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            if validarPrecio(nuevo_precio):
                guardarProducto(productos, producto_a_modificar, nuevo_precio)
                print("El nuevo precio de {} es {}\n".format(producto_a_modificar, nuevo_precio))
            else:
                print("El precio ingresado no es valido.\n")
        else:
            print("El producto ingresado no esta almacenado.\n")
            

### --- Programa principal --- ###
productos = {}

while True:
    opcion = mostrarMenu()

    if opcion == 1:
        agregarProducto(productos)
    elif opcion == 2:
        # Aca se podria poner la funcion mostrarProductos() dentro de la funcion modificarPrecio()
        # pero creo que con esta forma se entiende mas el comportamiento del programa
        mostrarProductos(productos)
        modificarPrecio(productos)
    elif opcion == 3:
        mostrarProductos(productos)  
    elif opcion == 4:
        print("Salio del programa.\n")
        break
    else:
        print("Operacion no valida.\n")