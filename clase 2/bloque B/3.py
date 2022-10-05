""" Escriba un programa que pida al usuario un valor entero n e
imprima un patrón triangular de n líneas como el que se muestra a
continuación: """

nro = int(input("Ingrese un número: "))
i = 1
while i <= nro:
    print("+"*i)
    i += 1