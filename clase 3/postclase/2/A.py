""" Escriba la función valida(cadena) que reciba un string con una cadena
de ADN y retorne True si la cadena es válida o False si no lo es. Una
cadena no es válida cuando aparecen bases nitrogenadas distintas a las
indicadas previamente (Adenina, Citosina, Guanina y Timina)
>>> valida(‘CTGA CTGA AATT GGGC CTGG CCCC’)
True
>>> valida(‘CTGA XCGA CGAT GGTA ACCC CCPC TTAA’)
False """

def valida(cadena):
    resultado = True
    validos = "ACGT "
    i = 0
    while i < len(cadena) and resultado:
        if cadena[i].upper() not in validos:
            resultado = False
        i += 1
    return resultado

def valida2(cadena):
    validos = "ACGT "
    for letra in cadena:
        if letra.upper() not in validos:
            resultado = False
            break
        else:
            resultado = True
    return resultado

""" print(valida("CTGA CTGA AATT GGGC CTGG CCCC"))
print(valida2("CTGA CTGA AATT GGGC CTGG CCCC"))

print(valida("CTGA XCGA CGAT GGTA ACCC CCPC TTAA"))
print(valida2("CTGA XCGA CGAT GGTA ACCC CCPC TTAA"))

print(valida("XCGA"))
print(valida2("XCGA")) """