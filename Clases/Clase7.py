## Manejo de cadena de caracteres

# las cadenas se peden procesar como una coleccion de caracteres
s = "cadena de caracteres"
print(s[0]) # imprimer la primera letra de la cadena
print(s[-1]) # imprime la ultima letra de la cadena

# slicing de cadenas
print(s[2:6]) # obtengo un substring que empieza en el caracter 2 y termina en el 5 (el 6 no esta incluido)
print(s[:6]) # substring que empieza en el caracter 0 y termina en el 5
print(s[7:]) # subtrinb que va del 7 hasta el final

# una cadena se puede recorrer con un for tambien
for letra in s:
    print(letra)

# comprar si una cadena comienza o termina con otra cadena
if s[:6] == "cadena":
    print("Si")

if s[10:] == "caracteres":
    print("Si")

# una forma mas facil de hacer esto es utilizando los metodos startswith y endswith:
if s.startswith("cadena"):
    print("si")

if s.endswith("caracteres"):
    print("si")

# metodo strip: sirve para eliminar espacios de adelante y de atras de un string
# tambien sirve para sacar los \n
continuar = input("Desea continuar? s/n: ")
if continuar.strip() == "s":
    print("sigue")

# los metodos devuelven un string nuevo, no pisan al string original.
# si quiero modificar el string original deberia hacer s = s.replace()
s2 = s.replace("caractetes", "eslabones")
print(s)
print(s2)


direccion = "San luis 345, Avellaneda, Buenos Aires"
s2 = direccion.split(",") # conjunto de caracteres con el cual quiero separar el string
# split devuelve una lista de strings

# si split("") lo dejo vacio, toma como default el espacio
# si pongo algo que no existe en el str, devuelve el str en una lista


# el metodo find sirve para buscar un substring en un string
# devuelve la posicion donde comienza esa cadena
pos = s.find("caracteres")

s3 = s.upper() # convierte el str a mayusculas
s4 = s.lower() # convierte el str a minusculas
s5 = s.capitalize() # pone el inicio de la cadena
s6 = s.title() # el inicio de cada palabra esta en mayusculas

### ----- ARGUMENTOS CLI ----- ###
#para levantar atributos por cli tengo que importar el modulo sys.
# ejecuto el programa: python programa.py arg1 agr2 arg3 ...

import sys
print(sys.argv)  # imprimo los argumentos que le paso desde cli


### ----- ARCHIVOS ----- ###
import os

print(os.listdir()) # retorna carpetas y directorios en el path del programa
print(os.getcwd()) # obtiene el current working directory

os.mkdir("path") # crea una carpeta en el path especificado
os.rmdir("path") # elimina una carpeta en el path especificado
os.rename("path1", "path2") # cambia el nombre del path1 al path2
os.remove("path") # elimina el archivo en el path especificado

# hay veces que os se "queda corto" para algunas tareas, es por eso que se importa
import shutil
shutil.copy("path1", "path2") # copia el arhivo del path1 al path2
shutil.move("path1", "path2") # mueve el archivo del path1 al path2
shutil.rmtree("path") # elimina el directorio y todo su contenido