#Escriba un programa que determine el área de un círculo a partir de su radio.
from xml.etree.ElementTree import PI

from math import pi

radio = float(input("Ingrese el radio de un círculo: "))
area = pi*radio**2
print("El área de la circunferencia es", round(area,2))