# Dado un Archivo separado con comas (.csv) con los siguientes campos: numDeProd, 
# Producto, Precio
# Ejemplo:
# 1, Computadora, 10000
# 2, Disco Duro 1TB, 5000
# 3, Teclado, 1000

# Generar las siguientes funcionalidades:
# 1- Cargar el archivo en una matriz
# 2- Generar las funciones de Alta, Baja y Modificación de los campos (ABM)
# 3- Generar un Listado de los productos
# 4- Al salir volcar la matriz modificada en el archivo
# 5- Agregar verificaciones a los campos


# Funcion que carga el archivo en una matriz
# Recibe como parametro la matriz y el nombre del archivo
def cargarArchivoAMatriz(matriz_productos, archivo):
    archivo = open(archivo, "r")

    # cargo el archivo en una matriz y separo los campos y elimino los espacios en blanco
    for linea in archivo.readlines():
        linea = linea.strip().split(",")
        matriz_productos.append(linea)

    # convierto los id a int y los precios a float
    for i in range(len(matriz_productos)):
        matriz_productos[i][0] = int(matriz_productos[i][0])
        matriz_productos[i][2] = float(matriz_productos[i][2])

    archivo.close()

# Funcion que da de alta un producto
# Recibe como parametro la matriz, el nombre del producto y el precio
def altaProducto(matriz_productos, producto, precio):

    # obtengo el utlimo id de los productos
    ultimo_id = int(matriz_productos[len(matriz_productos) - 1][0])

    # cargo el nuevo producto a la matriz
    matriz_productos.append([ultimo_id + 1, producto, precio])

# Funcion que da de baja un producto
# Recibe como parametro la matriz y el id del producto a dar de baja
def bajaProducto(matriz_productos, producto_id):

    if producto_id <= 0:
        raise ValueError("El numero del id debe ser mayor que cero")

    try:
        matriz_productos.pop(producto_id - 1)
    except:
        raise IndexError("No existe el producto con id: {}. \n".format(producto_id))

# Funcion que modifica el precio de un producto
# Recibe como parametro la matriz, el id del producto y el nuevo precio
def modificarPrecio(matriz_productos, producto_id, nuevo_precio):
    if type(nuevo_precio) != int and type(nuevo_precio) != float:
        raise ValueError("El precio debe ser un numero")
    
    try:
        matriz_productos[producto_id][2] = nuevo_precio
    except:
        raise IndexError("No existe el producto con id: {}. \n".format(producto_id))

# Funcion que muestra el listado de productos
# Recibe como parametro la matriz
def listadoProductos(matriz_productos):
    print("\n{:<10} {:<20} {:<10}".format("ID", "PRODUCTO", "PRECIO"))
    for i in range(len(matriz_productos)):
        print("{:<10} {:<20} {:<10}".format(matriz_productos[i][0], matriz_productos[i][1], matriz_productos[i][2]))
    print("\n")

# Funcion que guarda la matriz en el archivo
# Recibe como parametro la matriz de productos y el nombre del archivo
def guardarArchivo(matriz_productos, archivo):
    archivo = open(archivo, "w")
    for i in range(len(matriz_productos)):
        archivo.write("{},{},{}\n".format(matriz_productos[i][0], matriz_productos[i][1], matriz_productos[i][2]))
    archivo.close()

# Funcion que muestra el menu
def mostrarMenu():
    print("|-----------------------------------|")
    print("| 1 - Cargar Archivo.               |")
    print("| 2 - Alta Producto.                |")
    print("| 3 - Baja Producto.                |")
    print("| 4 - Modificar precio.             |")
    print("| 5 - Listado de productos.         |")
    print("| 6 - Salir y guardar.              |")
    print("|-----------------------------------|")
    opcion = int(input("Ingrese la operacion: "))
    return opcion


matriz_productos = []
while True:

    try:
        opcion = mostrarMenu()

    except ValueError:
        print("Debe ingresar un numero entero.\n")
        opcion = 0

    if opcion == 1:
        try:
            archivo = input("Ingrese el nombre del archivo con su extension: ")
            cargarArchivoAMatriz(matriz_productos, archivo)

        except FileNotFoundError:
            print("El archivo no existe. \n")

        except NameError:
            print("Error, no se puede realizar la operacion.")
            print("No se cargo ningun archivo.\n")

        except Exception as e:
            print("Error, {}".format(e))
        
        else:
            print("Archivo cargado con exito. \n")

    elif opcion == 2:
        try:
            if len(matriz_productos) == 0:
                raise NameError
            
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio: "))
            altaProducto(matriz_productos, producto, precio)

        except ValueError:
            print("El precio debe ser un numero")

        except NameError:
            print("Error, no se puede realizar la operacion.")
            print("No se cargo ningun archivo.\n")

        except Exception as e:
            print("Error, {}".format(e))

    elif opcion == 3:
        try:
            if len(matriz_productos) == 0:
                raise NameError
            
            listadoProductos(matriz_productos)
            producto_id = int(input("Ingrese el id producto a dar de baja: "))
            bajaProducto(matriz_productos, producto_id)

        except ValueError:
            print("El id del producto es un numero entero positivo. \n")
        
        except NameError:
            print("Error, no se puede realizar la operacion.")
            print("No se cargo ningun archivo.\n")

        except Exception as e:
            print("Error, {}".format(e))

    elif opcion == 4:
        try:
            if len(matriz_productos) == 0:
                raise NameError
            
            listadoProductos(matriz_productos)
            producto_id = int(input("Ingrese el id del producto a modificar: "))
            nuevo_precio = int(input("Ingrese el nuevo precio: "))
            modificarPrecio(matriz_productos, producto_id, nuevo_precio)
        
        except ValueError:
            print("El precio debe ser un numero")

        except NameError:
            print("Error, no se puede realizar la operacion.")
            print("No se cargo ningun archivo.\n")

        except Exception as e:
            print("Error, {}".format(e))
    
    elif opcion == 5:
        try:
            if len(matriz_productos) == 0:
               raise NameError
            
        except NameError:
            print("Error, no se puede realizar la operacion.")
            print("No se cargo ningun archivo.\n")
        
        else:
            listadoProductos(matriz_productos)

    elif opcion == 6:
        try:
            if len(matriz_productos) == 0:
               raise NameError
            
        except NameError:
            print("No se cargo ningun archivo.")
            print("Saliendo...")
            break
        else:
            guardarArchivo(matriz_productos, "archivo2.csv")
            print("Archivo guardado")
            print("Saliendo...")
            break
        
    else:
        print("Opcion incorrecta")