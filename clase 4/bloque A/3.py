""" Dos listas de números son ortogonales si su producto interno es cero. Escriba
la función son_ortogonales(a, b) que indique si a y b son ortogonales.
>>> son_ortogonales([2, 1], [-3, 6])
True """

def producto_interno(lista1, lista2):
    suma = 0
    i = 0
    while i < len(lista1):
        suma += lista1[i]*lista2[i]
        i += 1
    return suma


def son_ortogonales(a,b):
    return producto_interno(a,b) == 0

print(son_ortogonales([2, 1], [-3, 6]))