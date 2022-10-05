""" Escriba un programa que transforme una temperatura ingresada por usuario
de grados Farenheit (F) a Celsius (C), usando al siguiente fórmula: """

f = float(input("Temp. en Farenheit (F): "))
c = (f-32)*(5/9)
print("Los", f, "F en grados Celsius son", round(c), "C")