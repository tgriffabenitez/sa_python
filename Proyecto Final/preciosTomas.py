## Ejercicio final de Python ##
# Autor: Tomas Martin, Griffa Benitez (tgriffabenitez@gmail.com)

import sqlite3
import openpyxl
import os

### CLASES PARA EXCEPCIONES ###

# Clase para excepcion de ID inexistente
class IDNoExiste(Exception):
    pass


### FUNCIONES ###

# Funcion para mostrar el menu
def mostrarMenu():
    print("|----------------------------------------|")
    print("| 1 - Alta de Producto.                  |")
    print("| 2 - Baja de Producto.                  |")
    print("| 3 - Modificar Precio.                  |")
    print("| 4 - Listado de Productos Activos.      |")
    print("| 5 - Exportar en formato xlsx.          |")
    print("| 6 - Salir.                             |")
    print("|----------------------------------------|")
    opcion = int(input("Ingrese la operacion: "))
    return opcion


# Funcion para verificar si un producto existe en la base de datos
# Recibe el cursor y el ID del producto
# Devuelve True si existe, False si no existe
def existeProducto(cursor, producto):
    existe = True

    cursor.execute("SELECT * FROM precios WHERE IDProd = ? AND Estado = ?", (producto_id, True))
    fila = cursor.fetchone()

    if fila == None:
        existe = False
        
    return existe


# Funcion para dar de alta un producto en la base de datos
# Recibe el nombre del producto y el precio
def AltaProducto(producto, precio):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    if type(precio) != float:
        raise TypeError

    if precio <= 0:
        raise ValueError
    
    try:
        cursor.execute("INSERT INTO precios (Producto, Precio, Estado) VALUES (?, ?, ?)", (producto, precio, True))
    
    except sqlite3.IntegrityError:
        print("Error, el producto ya existe e la base de datos.\n")
        conn.close()

    except sqlite3.OperationalError:
        print("Error, la tabla no existe en la base de datos.\n")
        conn.close()

    except Exception:
        print("Error, no se pudo dar de alta el producto.")
        conn.close()
    
    else:
        print("Producto dado de alta con exito.\n")
        conn.commit()
        conn.close()


# Funcion para dar de baja logica un producto en la base de datos
# Recibe el ID del producto
def BajaProducto(producto_id):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    if type(producto_id) != int:
        raise TypeError("Error, el ID debe ser un numero positivo.\n")

    if producto_id <= 0:
        raise ValueError("Error, el ID debe ser un numero positivo.\n")

    try:
        # Verifico si el producto existe en la base de datos
        if existeProducto(cursor, producto_id):
            cursor.execute("UPDATE precios SET Estado = ? WHERE IDProd = ?", (False, producto_id))
            conn.commit()
            print("El producto se dio de baja correctamente.\n")
            conn.close()
        
        else:
            raise IDNoExiste("Error, el ID {} no existe en la base de datos.\n".format(producto_id))

    except Exception as e:
        print("{}".format(e))
        conn.close()


# Funcion para modificar el precio de un producto (que esta activo) en la base de datos
# Recibe el ID del producto activo a modificar y el nuevo precio
def ModificarPrecio(producto_id, precio):
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    if type(producto_id) != int:
        raise TypeError("Error, el ID debe ser un numero.\n")
    
    if producto_id <= 0:
        raise ValueError("Error, el ID debe ser un numero positivo.\n")

    if type(precio) != float:
        raise ValueError("Error, el precio debe ser un numero.\n")
    
    if precio <= 0:
        raise ValueError("Error, el precio debe ser un numero positivo.\n")

    try:
        # Verifico si el producto existe en la base de datos
        if existeProducto(cursor, producto_id):
            cursor.execute("UPDATE precios SET Precio = ? WHERE IDProd = ?", (precio, producto_id))
            conn.commit()
            print("El precio se modifico correctamente.\n")
            conn.close()
        
        else:
            raise IDNoExiste("Error, el ID {} no existe en la base de datos.\n".format(producto_id))
    
    except Exception as e:
        print("{}".format(e))
        conn.close()


# Funcion para listar los productos activos en la base de datos
def ListadoProductos():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT * FROM precios WHERE Estado = ?", (True,))
        
    except sqlite3.OperationalError:
        print("Error, no existe la tabla en la base de datos.\n")
        conn.close()

    except Exception as e:
        print("Error, {}".format(e))
        conn.close()

    else:
        print("\nListado de productos activos:")
        print("{:<5} {:<15} {:>10}".format("ID", "Producto", "Precio"))
        for fila in cursor:
            print("{:<5} {:<15} {:>10}".format(fila[0], fila[1], fila[2]))
        print()
        conn.close()


# Funcion que exporta los productos activos a un archivo xlsx
def ExportarXLSX():
    conn = sqlite3.connect("database.sqlite")
    cursor = conn.cursor()

    if os.path.exists("lista-de-precios.xlsx"):
        if input("El archivo lista-de-precios.xlsx ya existe. Desea sobreescribirlo? s/n: ").lower() != "s":
            print("Se cancelo la operacion.\n")
            conn.close()
            return
 
    try:
        cursor.execute("SELECT * FROM precios WHERE Precio >= ? AND Estado = ?", (1000, True))

    except sqlite3.OperationalError:
        print("Error, la tabla no existe en la base de datos.\n")
        conn.close()
        return
    
    except Exception as e:
        print("Error, {}".format(e))
        conn.close()
        return

    try:
        wb = openpyxl.Workbook()
        hoja = wb.active
        hoja.title = "Productos 1000+"
        hoja.append(("ID", "Producto", "Precio"))

        for fila in cursor:
            hoja.append((fila[0], fila[1], fila[2]))

        wb.save("lista-de-precios.xlsx")
        conn.close()

        print("Se exporto el listado de productos a lista-de-precios.xlsx.\n")

    except Exception:
        print("Error no se puedo exportar el listado de productos.\n")
        conn.close()


### PROGRAMA PRINCIPAL ###
while True:
    try:
        opcion = mostrarMenu()
    
    except ValueError as e:
        print("Error, la opcion debe ser un numero.\n")
        opcion = 0
        continue
        

    if opcion == 1:
        try:
            producto = input("Ingrese el nombre del producto: ")
            precio = float(input("Ingrese el precio del producto: "))
            AltaProducto(producto, precio)
        
        except ValueError:
            print("Error, el precio debe ser un numero positivo mayor a cero.\n")

        except TypeError as e:
            print("Error, el precio no puede ser igual a cero o negativo.\n")
        
        except Exception as e:
            print("Error, {}".format(e))


    elif opcion == 2:
        try:
            ListadoProductos()
            producto_id = int(input("Ingrese el ID del producto: "))
            BajaProducto(producto_id)
        
        except ValueError:
            print("Error, el ID debe ser de algun producto que este en la lista.\n")
        
        except TypeError:
            print("Error, el ID debe ser un numero.\n")

        except Exception as e:
            print("Error, no se pudo dar de baja el producto.\n")


    elif opcion == 3:
        try:
            ListadoProductos()
            producto_id = int(input("Ingrese el ID del producto: "))
            precio = float(input("Ingrese el nuevo precio del producto: "))
            ModificarPrecio(producto_id, precio)

        except ValueError:
            print("Error, el ID y el precio deben ser numeros.\n")
        
        except TypeError:
            print("Error, el ID y el precio deben ser numeros.\n")

        except Exception as e:
            print("Error, {}".format(e))


    elif opcion == 4:
        try:
            ListadoProductos()
        except Exception as e:
            print("Error, {}".format(e))


    elif opcion == 5:
        try:
            ExportarXLSX()
        
        except Exception as e:
            print("{}".format(e))
            print("Error, no se pudo exportar el listado de productos.\n")


    elif opcion == 6:
        print("Saliendo...\n")
        break


    else:
        print("Opcion invalida.\n")