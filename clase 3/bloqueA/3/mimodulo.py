def invertir_digitos(n):
    invertido = ''
    while n > 0:
        invertido = invertido + str(n % 10)
        n = n//10
    return invertido
