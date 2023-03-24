# Calculadora: Ingresar dos números y un operador(+,-,*,/) por consola e imprimir el
# resultado de la siguiente manera: Resultado: 3 + 4 = 7

operaciones = ["+", "-", "*", "/"]

num1 = float(input("Ingrese un numero: "))
op = input("Ingrese la operacion: " )
num2 = float(input("Ingrese un numero: "))

if op in operaciones:
	if op == "+":
		resultado = num1 + num2
	
	elif op == "-":
		resultado = num1 - num2
	
	elif op == "*":
		resultado = num1 * num2

	elif op == "/":
		if(num2 == 0):
			print("no se puede dividir por cero")
		else:
			resultado = num1 / num2
		
	print(num1, op, num2, " = ", resultado)
	
else:
	print("Operacion invalida")