""" Una fundación de ayuda a la comunidad está haciendo una campaña para la
recolección de dinero para poner máquinas de ejercicios en un parque. Para esto se
considera que podría haber un total de N benefactores o juntar un monto total de M
pesos (cualquiera de las dos condiciones se debe cumplir).

Escriba un programa que ingrese la cantidad total de benefactores N y el monto total
a recaudar M. Su programa debe solicitar el nombre y el monto que donará cada
benefactor, uno por uno. Su programa debe detenerse una vez que se alcance el
monto total M, o cuando se terminen de ingresar los N benefactores.

Indique cuál es el monto mayor donado y qué benefactor lo donó. """

N = int(input("Ingrese la cantidad de benefactores: "))
M = int(input("Ingrese el monto total en $: "))
print()


benefactores = 0
monto = 0

monto_mayor = -float('inf')
mayor_benefactor = ""

while benefactores < N and monto < M:
    nombre = input("Ingrese nombre del benefactor: ")
    donacion = int(input("Ingrese el monto de la donación: "))
    print("--------------------------")
    if donacion > monto_mayor:
        mayor_benefactor = nombre
        monto_mayor = donacion
        
    monto = monto + donacion
    benefactores += 1

print("El mayor monto donado es por", monto_mayor, "y fue donado por", mayor_benefactor)