""" Escriba la función cantidad(cadena, base) que reciba un string con una
cadena de ADN y una base nitrogenada. La función debe retornar la
cantidad de apariciones de la base en la cadena.
>>> cantidad(‘CTGA CTGA AATT GGGC CTGG CCCC’, ‘A’)
4 """

def cantidad(cadena, base):
    total = 0
    for letra in cadena:
        if letra.upper() == base.upper():
            total += 1
    return total

""" print(cantidad("CTGA CTGA AATT GGGC CTGG CCCC", "A")) """