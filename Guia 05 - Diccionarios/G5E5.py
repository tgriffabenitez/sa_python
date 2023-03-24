# Codifica un programa en Python que nos permita guardar los DNIs de los alumnos de una clase
# y las notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la
# información en un diccionario cuyas claves serán los DNIs de los alumnos y los valores serán listas
# con las notas de cada alumno.

# Realizar un menú que contenga las alternativas de alta de un alumno, alta de nota, tantas como se
# deban ingresar, listado de DNIs y promedios, informe de un alumno específico con DNI, notas y
# promedio.

diccionario = {}


while True:
    print("|----------------------------------------|")
    print("| 1 - Alta de Alumno.                    |")
    print("| 2 - Alta de Notas.                     |")
    print("| 3 - Listado DNI y Promedios.           |")
    print("| 4 - Informe de Alumno con DNI.         |")
    print("| 5 - Salir.                             |")
    print("|----------------------------------------|")
    opcion = int(input(">> Ingrese la operacion: "))
    print()

    notas = []

    if opcion == 1:
        while True:
            dni = int(input("Ingrese el DNI del alumno: "))
            if dni < 0:
                print("No se puede ingresar un dni negativo.\n")

            elif dni in diccionario:
                print("El alumno ya esta registrado.\n")

            else:
                diccionario[dni] = []
                print("Alumno agendado correctamente.\n")
                break    
                       
    elif opcion == 2:
        dni = int(input("Ingrese el DNI del alumno: "))
        if dni < 0:
            print("No se puede ingresar un dni negativo.\n")

        elif dni not in diccionario:
            print("No se encontro el alumno con el DNI ingresado.\n")

        else:
            while True:
                nota = int(input("Ingrese la nota del alumno: "))
                if nota < 0:
                    print("No puede ingresar una nota negativa: ")

                else:
                    notas.append(nota)
                    if input("Ingresar otra nota? s/n: ") == "n":
                        diccionario[dni] = notas
                        print()
                        break

    elif opcion == 3:
        print("{:<15} {:>10}".format("DNI", "Pormedio"))
        for alumno in diccionario:
            notas_alumno = diccionario[alumno]
            promedio_alumno = sum(notas_alumno)/len(notas_alumno)
            print("{:<15} {:>10.2f}".format(alumno, promedio_alumno))

    elif opcion == 4:
        dni = int(input("Ingrese el DNI del alumno: "))
        if dni < 0:
            print("No se puede ingresar un dni negativo.\n")

        elif dni not in diccionario:
            print("No se encontro el alumno con el DNI ingresado.\n")

        else:
            notas_alumno = diccionario[dni]
            promedio_alumno = sum(notas_alumno)/len(notas_alumno)

            print("DNI", dni)
            print("{}: {}".format("Promedio", promedio_alumno))
            print("Notas: ")
            for nota in notas_alumno:
                print(nota)
            print()
    
    elif opcion == 5:
        break

    else:
        print("Operacion no valida.")


# arreglar