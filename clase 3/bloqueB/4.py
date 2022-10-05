""" Cree una función codigo_hora(codigo) que reciba un código cifrado de
sólo números y el caracter ‘:’ y entregue el código descrifrado. La regla de
descifrado es la siguiente: sumar cada dígito anterior al caracter ‘:’ y
calcular el resto de la división entera entre esa suma y 24. Luego, lo mismo
con los dígitos después del carácter ‘:’, pero ahora el resto de la división es
entre esa suma y 60.
>>> codigo_hora(‘776199:68556’)
‘15:30’ """


def codigo_hora(codigo):
    suma1 = 0
    suma2 = 0
    pos = codigo.index(":")
    for n in codigo[:pos]:
        suma1 += int(n)
    for m in codigo[pos+1:]:
        suma2 += int(m)
    return str(suma1%24)+":"+str(suma2%60)

print(codigo_hora("776199:68556"))
    