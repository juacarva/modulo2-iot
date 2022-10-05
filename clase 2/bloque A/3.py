""" Escriba un programa que determine si un número es primo o
compuesto (no primo). """

num = int(input("Ingrese un número: "))
primo = True
i = 2
while primo and i < num:
    if num % i == 0:
        primo = False
    i += 1

if primo:
    print("El número es primo")
else:
    print("El numero es compuesto")