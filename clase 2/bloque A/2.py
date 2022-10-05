""" Escriba un programa que entregue todos los divisores de un número
entero ingresado. Su programa deberá validar que el número ingresado
sea positivo (> 0). En caso que cero o negativo, deberá mostrar un
mensaje de error. """

continuar = True
while continuar:
    num = int(input("Ingrese un número entero positivo: "))
    if num <= 0:
        continuar
        print("Error, debe ingresar un número mayor a 0")
    else:
        j = 1
        while j <= num:
            if num%j==0:
                print(j, end=" ")
            j = j+1
        continuar = False
        print()