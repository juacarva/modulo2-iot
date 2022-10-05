""" Un jugador debe lanzar dos dados numerados del 1 al 6, y su puntaje es la suma de
los valores obtenidos.

Un puntaje dado, puede ser obtenido con varias combinaciones posibles. Por
ejemplo, el puntaje 4 se logra con 3 combinaciones;1+3, 2+2, 3+1

Escriba un programa que pregunte al usuario un puntaje, y muestre como resultado
la cantidad de combinaciones con las que se puede obtener dicho puntaje. """

puntaje = int(input("Ingrese un puntaje (entre 2 y 12): "))
combinaciones = 0
i = 1
while i <= 6:
    j = 1
    while j <= 6:
        if i + j == puntaje:
            combinaciones +=1
        j += 1
    i += 1

print("Hay", combinaciones, "para obtener", puntaje)