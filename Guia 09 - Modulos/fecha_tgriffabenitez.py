## Modulo de fechas
# Autor: Tomas Martin, Griffa Benitez (tgriffabenitez)


# Funcion que valida una fecha ingresada
# Parametros: dia (int), mes (int), anio (int)
# Devuelve: True si la fecha es valida, False si no lo es
def es_valida(dia, mes, anio):
    # diccionario con los meses y sus dias
    meses = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    fecha_valida = True

    if type(dia) != int or type(mes) != int or type(anio) != int:
        raise TypeError("Debe ingresar un numero entero")
    
    if (dia >= 1 and dia <= 31) and (mes >= 1 and mes <= 12) and (anio >= 1930):
        if mes == 2 and es_bisiesto(anio):
            if dia > 29:
                fecha_valida = False
        else:
            if dia > meses[mes]:
                fecha_valida = False
    else:
        fecha_valida = False

    return fecha_valida


# Funcion que devuelve el mes en texto
# Parametros: numero
# Devuelve: el mes en texto
def mes_por_numero(numero):
    meses = {1:"Enero", 2:"Febrero", 3:"Marzo", 4:"Abril", 5:"Mayo", 6:"Junio", 7:"Julio", 8:"Agosto", 9:"Septiembre", 10:"Octubre", 11:"Noviembre", 12:"Diciembre"}
    
    if type(numero) != int:
        raise TypeError("Debe ingresar un numero entero")
    
    if numero > 12 or numero < 1:
        return ""
    
    return meses[numero]


# Funcion que valida si un anio es bisiesto
# Parametros: anio
# Devuelve: True si el anio es bisiesto, False si no lo es
def es_bisiesto(anio):
    es_anio_bisiesto = False

    if type(anio) != int:
        raise TypeError("Debe ingresar un numero entero")

    # si un anio es divisible entre 4 pero no entre 100, entonces el anio es bisiesto
    # los anios divisibles por 400 tambien sos bisiestos
    if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
        es_anio_bisiesto = True

    return es_anio_bisiesto



