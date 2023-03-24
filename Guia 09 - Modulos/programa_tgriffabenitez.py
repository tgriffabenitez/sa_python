# Programa para validar el modulo de fecha_tgriffabenitez
import fecha_tgriffabenitez as fecha

print("*** Programa para probar el modulo de fecha ***")
try:
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el anio: "))

    if fecha.es_valida(dia, mes, anio) and fecha.es_bisiesto(anio):
        print("{} de {} de {} - es bisiesto".format(dia, fecha.mes_por_numero(mes), anio))
    
    elif fecha.es_valida(dia, mes, anio) and not fecha.es_bisiesto(anio):
        print("{} de {} de {} - no es bisiesto".format(dia, fecha.mes_por_numero(mes), anio))
    
    else:
        print("La fecha no es valida")

except ValueError:
    print("Error, debe ingresar un numero.\n")

except Exception as e:
    print("Error, {}".format(e))