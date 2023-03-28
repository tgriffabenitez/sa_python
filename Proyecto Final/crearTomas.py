## Script para crear y cargar la base de datos ##
# Autor: Tomas Martin, Griffa Benitez (tgriffabenitez@gmail.com)

import sqlite3

conn = sqlite3.connect("database.sqlite")
cursor = conn.cursor()

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
        print("Se sobreescribio la tabla precios\n")
    else:
        print("No se sobreescribio la tabla precios\n")
        conn.close()

except Exception as e:
    print("Error, No se pudo crear la tabla de precios")
    print("{}".format(e))
    conn.close()

else:
    productos = (
        ("Computadora", 10000, True), 
        ("Disco Duro 1TB", 5000, True), 
        ("Monitor 24", 7000, True),
        ("Mouse", 500, True),
        ("Teclado", 900, True),
        ("Parlantes", 2000, True),
        ("Impresora", 8000, True),
        ("Router", 3000, True))

    # cargo los productos en la tabla precios
    for producto, precio, estado in productos:
        cursor.execute("INSERT INTO precios (Producto, Precio, Estado) VALUES (?, ?, ?)", (producto, precio, estado))

    conn.commit()
    conn.close()
    print("Se creo la tabla precios y se cargaron los productos.\n")