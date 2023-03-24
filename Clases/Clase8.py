

import subprocess

# esta linea de codigo es lo mismo que poner en el cmd
# mkdir python clase 22
# creo una carpeta que se llama: python clase 22
# subprocess.run(["mkdir", "python clase 22"], shell=True)

# para obtener el nombre del host, debemos usar
# con el capture_output=True, "agarro" lo que me devuelve la consola y lo guardo en resultado
resultado=subprocess.run("hostame", capture_output=True, encoding="cp850")
print(resultado.stdout)

resultado=subprocess.run(["C:\\Python311\\python.exe", "--version"], capture_output=True, encoding="cp850")