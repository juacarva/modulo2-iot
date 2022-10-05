""" Escriba un programa que permita determinar el número mayor de n
números solicitados al usuario. """

n = int(input("Cantidad de números: "))

mayor = -float('inf')
posicion = 0
i = 0
while i < n:
    nro = float(input("Ingrese numero "+ str(i+1)+": "))
    if nro > mayor:
        mayor = nro
        posicion = i + 1
    i += 1
print("El mayor es "+ str(round(mayor,1)) +" que corresponde al número "+ str(posicion))