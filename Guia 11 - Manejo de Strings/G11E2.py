# Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de
# apariciones de cada carácter en la cadena.

s = "Escribe un programa que lea una cadena y devuelva un diccionario con la cantidad de apariciones de cada carácter en la cadena."
diccionario = {}
for letra in s:
    if letra in diccionario:
        diccionario[letra] += 1
    else:
        diccionario[letra] = 1

print(diccionario)