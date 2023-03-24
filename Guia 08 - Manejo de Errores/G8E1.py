# A partir del siguiente diccionario de empleados
# Imprimir los datos de un empleado que podrá ser buscado por número de legajo o por apellido.
# En el caso de búsqueda por apellido mostrar ***** si no tiene segundo nombre y contabilizar los
# empleados con segundo nombre.

empleados={"100":{"nombre":"Juan","segundo":"Carlos","apellido":"Nunez"},
           "201":{"nombre":"Elvira","apellido":"Goldstein"},
           "202":{"nombre":"Ana","segundo":"Laura","apellido":"Gonzalez"},
           "102":{"nombre":"Ignacio","apellido":"Nunez"}}

# Clase personalizada para lanzar la except.
class EmpleadoNoEncontrado(Exception):
    pass

# Funcion que imprime el menu de opciones
# Devuelve la opcion seleccionada por el usuario
def imprimirMenu():
    print("|---------------------------------------------------------|")
    print("| 1 - Buscar por legajo.                                  |")
    print("| 2 - Buscar por Apellido.                                |")
    print("| 3 - Consultar cuantas personas tiene segundo nombre     |")
    print("| 4 - Salir.                                              |")
    print("|---------------------------------------------------------|")
    opcion = int(input("Ingrese la opcion: "))
    return opcion

# Funcion que imprime los datos del empleado
# Recibe un diccionario con los datos del empleado
# En caso que el empleado no tenga segundo nombre
# se imprime **** en su lugar
def imprimirEmpleado(empleado):
    print("Nombre:", empleado["nombre"])
    if "segundo" in empleado:
        print("Segundo:", empleado["segundo"])
    else:
        print("Segundo: *****")
    print("Apellido:", empleado["apellido"])
    print()


# Funcion que cuenta los empleados que tienen segundo nombre
# Recibe un diccionario de diccionarios de empleados
# Devuelve el total de empleados con segundo nombre
def contarSegundosNombres(empleados):
    total = 0
    for legajo in empleados:
        if "segundo" in empleados[legajo]:
            total += 1
    print("En total hay {} personas con segundo nombre.".format(total))


# Funcion que busca un empleado segun su legajo
# Recibe un diccionrio de empleados y el legajo (key) a buscar
# Devuelve el empleado buscado. En caso de no encontrarlo, lanza una except.
def buscarPorLegajo(empleados, legajo):
    try:
        empleado_encontrado = empleados[legajo]
    except:
        raise EmpleadoNoEncontrado()
    else:
        return empleado_encontrado

# Funcion que busca un empleado segun su apellido
# Recibe un diccionrio de empleados y el apellido a buscar
# Devuelve una lista con empleados que tienen el apellido buscado
def buscarPorApellido(empleados, apellido):
    empleados_apellido = []
    for legajo in empleados:
        try:
            if empleados[legajo]["apellido"] == apellido:
                empleados_apellido.append(empleados[legajo])
        except:
            raise EmpleadoNoEncontrado()
    return empleados_apellido

while True:
    try:
        opcion = imprimirMenu()
    except ValueError:
        print("Ingrese un numero valido\n")
        opcion = 0 # Para que vuelva a entrar al while

    if opcion == 1:
        empleado_id = input("Ingrese el legajo del empleado: ")
        try:
            empleado_encontrado = buscarPorLegajo(empleados, empleado_id)
        except EmpleadoNoEncontrado:
            print("No se encontro el empleado con el id:", empleado_id)
            print("\n")
        else:
            imprimirEmpleado(empleado_encontrado)

    elif opcion == 2:
        empleado_apellido = input("Ingrese el apellido del empleado: ")
        try:
            empleado_encontrado = buscarPorApellido(empleados, empleado_apellido)
        except EmpleadoNoEncontrado:
            print("No se encontro el empleado con el apellido:", empleado_apellido)
            print("\n")
        else:
            for empleado in empleado_encontrado:
                imprimirEmpleado(empleado)

    elif opcion == 3:
        contarSegundosNombres(empleados)

    elif opcion == 4:
        print("Salio del programa")
        break

    else:
        print("Operacion no valida")