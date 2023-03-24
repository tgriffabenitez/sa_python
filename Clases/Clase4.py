## Funciones

# para definir las funciones en python se usa la palabra reservada "def"
# seguido del nombre de dicha funcion con sus parametros

def sumar1(num1, num2):
    total = num1 + num2
    print(total)

def sumar2(num1, num2):
    return (num1 + num2)

a = 4
b = 9
sumar1(a, b) # llamo a la funcion

resultado = sumar2(a, b)
print(resultado)

# que pasa si tengo que sumar mas de dos argumentos?
c = 10
resultado = sumar2(sumar2(a, b), c)
print(resultado)

# dentro de las funciones puedo dejar fijo un valor en caso que el usuario no lo ingrese
def sumar3(num1 = 15, num2 = 20):
    return (num1 + num2)

a = 5
b = 10

# si llamo a sumar3 solo, pasa esto:
print(sumar3()) # devuelve 35

# si quiero cambiar el numero de num1 puedo hacer:
print(sumar3(num1=a)) # devuelve 25
print(sumar3(num2=5)) # devuelve 20


# para modificar una variable global a nivel local, hay que utilizar el keyword "global"
a = 2 # la variable global a vale 2
def funcion():
    global a
    a = 4 # ahora la variable a vale 4
    print(a)

funcion()
print(a) # la variable a sigue valiendo 4
