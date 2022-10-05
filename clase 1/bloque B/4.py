""" Escriba un programa que considere la siguiente tabla para mostrar el total
de impuestos a pagar por una persona según su sueldo.


Sueldo                              |   Tasa de impuesto

Menos de 1000                       |   0%
Entre 1000 y 2000(sin incluirlo)    |   5%
Entre 2000 y 4000(sin incluirlo)    |   10%
4000 o más                          |   12% """

sueldo = int(input("Ingrese su sueldo: "))

if sueldo < 1000:
    tasa = 0
elif sueldo >= 1000 and sueldo < 2000:
    tasa = 0.05
elif sueldo >= 2000 and sueldo < 4000:
    tasa = 0.1
else:
    tasa = 0.12

print("Usted pagará", round(tasa*sueldo), "de impuesto")