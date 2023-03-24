# ~ C8- Python también se utiliza en IoT(Internet de las Cosas) por ejemplo para programar
# ~ entradas y salidas en Raspberry Pi, nodeMCU, ESP32 entre otras plataformas. Utilizando
# ~ el circuito con interruptores, en serie y paralelo, y una lámpara, indicar por mensajes en
# ~ consola cuando la lámpara está encendida o no. Los interruptores deben ser simulados
# ~ con entradas por consola. Se debe llegar a un único estado “lámpara encendida” u a un
# ~ único estado “lámpara apagada”.

estaEnchufado = int(input("esta enchufado: " ))

if (estaEnchufado):
	switchA = int(input("estado switchA: "))
	switchB = int(input("estado switchB: "))
	switchC = int(input("estado switchC: "))
	
	if ((switchA) or (switchB and switchC)):
		print("Lampara prendida")
	else:
		print("Lampara apagada")
else:
    print("No hay tension en la red")