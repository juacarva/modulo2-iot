""" A partir de un número cualquiera (entrada) es posible hacer una sucesión de
números que termina en 1, para ello deberá seguir las siguientes instrucciones:

- Si el número es par, se debe dividir por 2
- Si el número es impar, se debe multiplicar por 3 y sumarle 1.

Con esto se obtiene el siguiente número de la sucesión, al cual se le aplican las
mismas operaciones. La sucesión termina cuando el número obtenido es 1.

Escriba un programa que muestre cada número de la sucesión generada, hasta
llegar a 1. """

nro = int(input("Ingrese un número: "))

while nro != 1:
    if nro % 2 == 0:
        nro = nro / 2
    else:
        nro = nro * 3 +1
    print(int(nro), end=" ")
print()
