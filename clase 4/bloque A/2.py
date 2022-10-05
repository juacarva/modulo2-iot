""" El producto interno de dos listas de números es la suma de los productos de
los términos de ambas. Por ejemplo, si: a = [5, 1, 6] y b = [1, -2, 8]
entonces el producto interno entre a y b es: (5 * 1) + (1 * -2) + (6 * 8)
Escriba la función producto_interno(a, b) que entregue el producto interno
entre a y b.
>>> a = [7, 1, 4, 9, 8]
>>> b = range(5)
>>> producto_interno(a, b)
68 """

def producto_interno(lista1, lista2):
    if len(lista1)==len(lista2):
        suma = 0
        i = 0
        while i < len(lista1):
            suma += lista1[i]*lista2[i]
            i += 1
        return suma
    else:
        return "Error!! No es posible hace el producto interno. Compruebe los largos de las listas."

a = [7, 1, 4, 9, 8]
b = range(5)

print(producto_interno(a, b))