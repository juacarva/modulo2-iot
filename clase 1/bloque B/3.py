""" Escriba un programa que reciba como entrada la estatura, el peso y
la edad de una persona, y el entregue la condición de riesgo.
Considere que el IMC se calcula como: peso / estatura ** 2

El riesgo está determinado por la siguiente tabla:

                Edad < 45   |   Edad >= 45
                ___________________________
IMC < 22.0      Bajo        |   Medio
IMC >= 22.0     Medio       |   Alto """

estatura = float(input("Ingrese la estatura (mt): "))
peso = float(input("Ingrese el peso (kg): "))
edad = int(input("Ingrese la edad: "))

IMC = peso / estatura**2

if edad < 45:
    if IMC < 22:
        print("Riesgo Bajo")
    else:
        print("Riesgo Medio")
else:
    if IMC < 22:
        print("Riesgo Medio")
    else:
        print("Riesgo Alto")
