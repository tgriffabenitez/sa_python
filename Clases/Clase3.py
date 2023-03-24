## Tuplas >> ordenadas pero no modificables

# las tuplas se definen con parentesis y los elementos se separan con coma
tupla_uno = (10, 20, 30, 40)
tupla_tres = (3, 6, 7, 13)

# las tuplas de un solo elemento, debe tener despues del ultimo elemento una coma
tupla_dos = (3,)

# para obtener un valor de una tupla
print(tupla_uno[1])

# para obtener el largo de una tupla
print(len(tupla_uno))

# las tuplas se pueden sumar para juntarlas
tupla_cuatro = tupla_uno + tupla_tres
print(tupla_cuatro)

# se pueden recorrer en un for
for elemento in tupla_cuatro:
    print(elemento)

for pos in range(len(tupla_uno)):
    print(tupla_uno[pos])

# (unpacking) desempaquetado de tuplas
tupla_nombre = ("Juan", "Carlos", "Protto")

nombre, seg_nombre, apellido = tupla_nombre
print(nombre + " " + seg_nombre + " " + apellido)


## Diccionarios
# No son ordenados y son manipulables
# estan compuestos por una clave y valor.
#diccionario = {clave1 : valor1, clave2 : valor2, ..., claven: valorn}

diccionario = {"nombre":"Romina", "edad":30}
print(diccionario["nombre"])
print(diccionario["edad"])

# los diccionarios si se pueden modificar
diccionario["edad"] = 45
print(diccionario["edad"])

# para agregar un nuevo elemento al diccionario hay que agregarlo de a pares
diccionario["DNI"] = 32759174
diccionario[123] = 100

print(diccionario)


## set (conjunto)
# no respeta el orden de los elementos. Cuando lo imprimo puede que salgan ordenados o no
conjunto = {4, 6, 8, 3, 9, 2}
lista = [10, 20, 30, 40, 10 ,20]

# como una lista puede tener valores repetidos y los sets no, puedo castear
# una lista a un set para eliminar los repetidos. Ahora pierdo el formato de lista
unicos = set(lista)

# para volver al formato de lista, puedo castear el set a una lista
print(list(unicos(lista)))

# funciones utiles para colecciones

min(lista)    # valor minimo de una coleccion
max(lista)    # valor maximo de una coleccion
sum(lista)    # suma los valores numeros de una coleccion
sorted(lista, reverse = True) # ordena los elementos de una coleccion