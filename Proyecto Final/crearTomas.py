## Script para crear y cargar la base de datos ##
# Autor: Tomas Martin, Griffa Benitez (tgriffabenitez@gmail.com)

import sqlite3

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

productos = (
        ("Computadora", 10000, True), 
        ("Disco Duro 1TB", 5000, True), 
        ("Monitor 24", 7000, True),
        ("Mouse", 500, True),
        ("Teclado", 900, True),
        ("Parlantes", 2000, True),
        ("Impresora", 8000, True),
        ("Router", 3000, True))



# Funcion para cargar la tabla de precios
# Recibe la lista de productos
def cargarBD(productos):
    # cargo los productos en la tabla precios
    for producto, precio, estado in productos:
        cursor.execute("INSERT INTO precios (Producto, Precio, Estado) VALUES (?, ?, ?)", (producto, precio, estado))

    conn.commit()
    conn.close()
    print("Se cargaron los productos.\n")


try:
    # creo la tabla de precios
    cursor.execute("CREATE TABLE precios (IDProd INTEGER PRIMARY KEY AUTOINCREMENT, Producto TEXT, Precio NUMERIC, Estado BOOLEAN)")
    
except sqlite3.OperationalError:
    # si la tabla ya existe, pregunto si la quiero sobreescribir
    print("Ya existe la tabla precios.")
    if input("Desea sobreescribirla? (s/n): ").lower() == "s":
        # borro la tabla y la vuelvo a crear
        cursor.execute("DROP TABLE precios")
        cursor.execute("CREATE TABLE precios (IDProd INTEGER PRIMARY KEY AUTOINCREMENT, Producto TEXT, Precio NUMERIC, estado BOOLEAN)")
        cargarBD(productos)
    else:
        print("No se sobreescribio la tabla precios\n")
        conn.close()

except Exception as e:
    print("Error, No se pudo crear la tabla de precios")
    print("{}".format(e))
    conn.close()

else:
    cargarBD(productos)