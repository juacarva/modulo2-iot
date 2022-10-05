""" Los científicos encontraron un patrón de clasificación, que se deduce de la cantidad
mayoritaria de cierto grupo de bases. Si la suma de las cantidades de Citosina y Guanina
es mayor a la de Adenina y Timina, es una especie vegetal, en caso contrario es una
especie animal. Escriba un programa que pregunte la cantidad de cadenas de ADN a
evaluar, luego solicite las cadenas y finalmente muestre las cantidades de cada especie
y cadenas no válidas. Use las funciones anteriores.
Cantidad de cadenas a ingresar: 3
Ingrese cadena 1: CGTA CAGT TTGG GGTA AATG CATG
Ingrese cadena 2: CACC CTGA GGAA ACAA XTFC ATGG
Ingrese cadena 3: TGTG TTGA ATGA CTAT ATTT
Cantidad animales: 2
Cantidad vegetales: 0
Cantidad no validas: 1 """

from A import valida
from B import cantidad

print(valida("CTGA CTGA AATT GGGC CTGG CCCC"))
print(cantidad("CTGA CTGA AATT GGGC CTGG CCCC", "A"))

n = int(input("Cantidad de cadenas a ingresar: "))

animales = 0
vegetales = 0
invalidas = 0
i = 1
while i <= n:
    cadena = input("Ingrese cadena "+str(i)+":")
    if valida(cadena):
        at = cantidad(cadena,"A") + cantidad(cadena,"T")
        cg = cantidad(cadena,"C") + cantidad(cadena,"G")
        if at > cg:
            animales += 1
        elif cg > at:
            vegetales += 1
    else:
        invalidas += 1
    i += 1

print("cantidad animales:", animales)
print("cantidad vegetales:", vegetales)
print("cantidad no válidas:", invalidas)



