# Imprimir todas las ocurrencias de espacios en este enunciado utilizando find.

s = "Imprimir todas las ocurrencias de espacios en este enunciado utilizando find."

pos = s.find(" ")
while pos > -1:
    print(pos)
    pos = s.find(" ", pos + 1)
    