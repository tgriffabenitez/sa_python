### Exceptions

# En el bloque try: solo va el codigo que queremos verificar. No hace falta poner todo el codigo de la funcion.
try:
    print(int("HOLA"))

except ValueError:
    print("Ocurrio un error")

# Al igual que en java, se pueden poner varios except dependiendo el tipo de error que queremos atrapar
try:
    print(int([1, 2, 3]))
except ValueError:
    print("Ocurrio un error: Valor incorrecto")
except TypeError:
        print("Ocurrio un error: tipo de dato incorrecto")

# Otra forma de agregar varios except, es agregando una tupla de errores.
# Esta forma es menos "personalizada" ya que va a tratar a todos los errores de
# la misma forma
try:
    print(int([1, 2, 3]))

except (ValueError, TypeError):
    print("Ocurrio un error")


# El error en este codigo, el error los produce el lista[i].
# el for no genera el error, el for funciona bien.
# dentro del try solamente iria el print(lista[i])
lista = [10, 20, 30, 40]
for i in range(0, 5):
    try:
        print(lista[i])
    except IndexError:
        print("Fuera de rango en i:", i)

producto = {"id": 100, "nombre": "televisor", "precio": 234}

try:
    print(producto["nro_serie"]) # devuelve una exception del tipo KeyError
except KeyError:
    print("No existe esa clave")

# con el except Exception se puede atrapar cualquier tipo de exception
# es menos personalizable porque todas las exceptions las va a tratar igual

def sumar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise TypeError("Se requieren dos numeros")
    total = num1 + num2
    return total

try:
    sumar(2, "a")
except Exception: # atrapo el TypeError
    print("No se pudo sumar")


# Puedo crearme calses personalizadas para errores
class NoNumError(Exception):
    pass

def sumar(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        raise NoNumError("Se requieren dos numeros")
    total = num1 + num2
    return total

try:
    sumar(2, "a")
except NoNumError: # atrapo el TypeError
    print("No se pudo sumar")

