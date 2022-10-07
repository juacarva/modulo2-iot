""" Escriba un programa que abra el archivo quijote.txt y cuente:
- Cuántas letras tiene
- Cuántas palabras tiene
- Cuántas líneas tiene """


archivo = open("quijote.txt", "r")
letras = 0
palabras = 0
lineas = 0
for linea in archivo:
    palabras += len(linea.split())

print(palabras)
