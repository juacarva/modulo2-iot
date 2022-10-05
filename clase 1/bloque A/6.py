""" Escriba un programa que calcule el área de un triángulo a partir de la
longitud de sus lados (a, b y c), y de su semiperímetro (s)"""

from cmath import sqrt


a = float(input("Ingrese longitud lado 1: "))
b = float(input("Ingrese longitud lado 2: "))
c = float(input("Ingrese longitud lado 3: "))

s = (a + b + c)/2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)

print("El área del triángulo es:", round(area,2))