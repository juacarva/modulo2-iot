""" Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número
ingresado por el usuario. """

num = int(input("Ingrese un número: "))
contador = 1
while contador <=10:
    print(num,"x",contador,"=", contador*num)
    contador += 1