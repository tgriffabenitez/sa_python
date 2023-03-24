# Supongamos que tenemos $10000, que podemos invertir obteniendo el 10% de
# interés cada año.
# Luego del primer año, tendremos $10000 x 1.1, luego de dos años tendremos $10000 x
# 1.1 x 1.1.
# Solicitar importe de inversión y cantidad de años, calcular y mostrar el importe final de
# cada año incluyendo intereses.

TASA_INTERES = 1.1

capital = float(input("Ingrese el capital a invertir: "))
cantidad_anios = int(input("Ingresar los años de inversión: "))

for i in range(1, cantidad_anios + 1):
    total_acumulado = capital * (TASA_INTERES) ** i
    interes_acumulado = total_acumulado - capital
    print("En el año", i, "el total acumulado es:", round(total_acumulado, 2), "y el interés acumulado es:", round(interes_acumulado, 2))