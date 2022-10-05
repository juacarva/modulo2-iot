""" Escriba un programa que permita ingresar 5 números enteros y
determine cuál de los cuatro números es el más lejano al primero. """

num = int(input("Primer número: "))
n1 = int(input("Ingrese número: "))
n2 = int(input("Ingrese número: "))
n3 = int(input("Ingrese número: "))
n4 = int(input("Ingrese número: "))

d1=abs(num-n1)
d2=abs(num-n2)
d3=abs(num-n3)
d4=abs(num-n4)



if d1>d2 and d1>d3 and d1>d4:
    print("El número más lejano al primero es", n1)
elif d2>d1 and d2>d3 and d2>d4:
    print("El número más lejano al primero es", n2)
elif d3>d1 and d3>d2 and d3>d4:
    print("El número más lejano al primero es", n3)
else:
    print("El número más lejano al primero es", n4)