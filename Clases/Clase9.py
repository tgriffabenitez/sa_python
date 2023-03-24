## Escritura de archivos ##

# para trabajar con archivos, tenemos que usar un objeto archivo
archivo = open("archivo.txt", "w") # w es para "write" escribir en el archivo
archivo.write("texto a escribir\n") # con .write() se escribe en el archivo
archivo.close() # cierra el archivo

# para escribir agregarle mas informacion al archivo se usa el append
archivo = open("archivo.txt", "a")
archivo.write("nueva linea\n")
archivo.write("otra nueva linea")
archivo.close()

# si por ejemplo quiero escribir una lista en un archivo puedo usar
lista = ["hola\n", "chau\n"]
archivo = open("archivo.txt", "a")
archivo.writelines(lista)
archivo.close()

## Lectura de archivos ##

# de esta forma leo la totalidad del archivo, no es muy util si estamos
# trabajando con un archivo muy grande
archivo = open("archivo.txt", "r")
saludo = archivo.read()
print(saludo)
archivo.close()

# es mejor ir leyendo el archivo liea por linea. Esto solo lee la primer linea
# necesito hacer un loop para leer todas las lineas del archivo
archivo = open("archivo.txt", "r")
linea = archivo.readline()
print(linea)
archivo.close()

# ejemplo con while
archivo = open("archivo.txt", "r")
linea = archivo.readline()
while linea != "":
    print(linea)
    linea = archivo.readline()
archivo.close()

# ejemplo con for
archivo = open("archivo.txt", "r")
for linea in archivo.readlines():
    print(linea)
archivo.close()

# en caso que tenga que contar las lineas o enumerarlas, puedo hacer
archivo = open("archivo.txt", "r")
contador = 1
for linea in archivo.readlines():
    print("{}: {}".format(contador, linea))
    contador += 1
archivo.close()

# otra forma de contar las lineas seria
archivo = open("archivo.txt", "r")
for contador, linea in enumerate(archivo.readlines(), 1): # con el 1 indico de donde empiezo a contar
    print("{}: {}".format(contador, linea))
archivo.close()


## BASE DE DATOS ##
import sqlite3
conn = sqlite3.connect("database.sqlite") # se pone el nombre de la base de datos, si no existe, la crea
cursor = conn.cursor() # indica en "donde estamos parados" en la base de datos

# para realizar una consulta sql, hay que usar el cursor
cursor.execute("CREATE TABLE personas (nombre TEXT, edad Numeric)")
conn.commit() # se usa para confirmar la modificacion
conn.close() # cierra la base de datos