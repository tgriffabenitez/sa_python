## BASE DE DATOS ##
import sqlite3
conn = sqlite3.connect("database.sqlite") # se pone el nombre de la base de datos, si no existe, la crea
cursor = conn.cursor() # indica en "donde estamos parados" en la base de datos

personas =(("Juan", 20), ("Maria", 30), ("Pedro", 40))

for nombre, edad in personas:
    cursor.execute("INSERT INTO personas VALUES (?, ?)", (nombre, edad)) # los ? son comodines
conn.commit() # se usa para confirmar la modificacion
conn.close() # cierra la base de datos

# Para traer valores de una base de datos se usa la consulta SELECT
cursor.execute("SELECT * FROM persona")
personas = cursor.fetchall() # trae todos los datos

# hago un unpacking para mostar los valores obtenidis
for persona, edad in personas:
    print("{} - {}".format(nombre, edad))
conn.close()

# Para traer un unico valor de la base de datos, podemos hacer
cursor.execute("SELECT count(*) FROM personas")
cantidad = cursor.fetchone() # devuelve una tupla con un solo valor
print(cantidad[0]) #imprimo el "la posicion correcta" de la tupla
conn.close()

## En esta libreria se debe manejar el except: sqlite3-OperationError

try:
    cursor.execute("CREATE TABLE personas (nombre TEXT, edad NUMERIC)")
except sqlite3.OperationalError:
    print("La existe la base de datos")

## Para ejecturas varias operacines juntas se puede usar el conn.executescripts()


## COMO USAR Pymysql ##
import pymysql
import clave

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = clave.CLAVE_MYSQL,
    databse = "python"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE personas(nombre VARCHAR(60), edad INT)")

personas =(("Juan", 20), ("Maria", 30), ("Pedro", 40))

for nombre, edad in personas:
    cursor.execute("INSERT INTO personas VALUES(%s, %s)", (nombre, edad))

cursor.execute("SELECT * FROM persona")
personas = cursor.fetchall()

cursor.execute("SELECT count(*) FROM personas")
cantidad = cursor.fetchone()
print(cantidad[0])
conn.close()

conn.commit()
conn.close()


# en sqlite, para indicar que el id sea autoincrementa hay que hacer lo siguiente
cursor.execute("CREATE TABLE nombres (id INTEGER, nombre TEXT primary key(id))")


### openpyxl ###
import openpyxl

alumnos = [("juan", "gomez", 20), ("maria", "perez", 30), ("pedro", "ramirez", 40), ("jose", "lopez", 50)]

wb = openpyxl.Workbook()
hoja = wb.active()
hoja.title = "Alumnos"

hoja.append(("Nombre", "Apellido", "DNI", "Cursos"))

for alumno in alumnos:
    hoja.append(alumno)

wb.save("curso.xml")

# doc string #

#si yo creo una funcion
def funcion():
    """
    y escribo esto asi, cuando el usuario hago funcion() --help en la consola,
    le va a salir este texto como documentacion
    """

## CLASES Y OBJETOS ##

class MiClase1:
    def __init__(self): # este es el constructor de la clase
        self.a = 1
        print("has creado una instancia de MiClase")

objeto_1 = MiClase1()
print(objeto_1.a) #imprimo el valor de a, 1

class MiClase2:
    def __init___(self, desde_afuera):
        self.a = desde_afuera
    
    def imprimir_a(self):
        print(self.a)

objeto_2 = MiClase2()
objeto_2.imprimir_a()


class MiClase3():
    def publico(self):
        print("Accediendo a un metodo publico")
    
    def __privado(self):
        print("Accediendo a un metodo privado")


class Padre():
    apellido = "Griffa"

    def leer(self):
        print("La persona sabe leer")

class Hijo(Padre):
    def programar(self):
        print("La persona sabe programar")

persona = Hijo()
print(persona.apellido)
persona.leer()
persona.programar()