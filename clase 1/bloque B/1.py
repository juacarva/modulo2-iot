""" Escriba un programa que genere aleatoriamente el lanzamiento de
una moneda y muestre por pantalla su resultado (CARA o SELLO). """

from random import randint

moneda = randint(0,1)
if moneda:
    print("SELLO")
else:
    print("CARA")