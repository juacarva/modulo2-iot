""" Cree una función codigo_palabra(codigo) que reciba un código cifrado de sólo
letras y entregue el mensaje descifrado. La regla de descifrado es la siguiente: la
palabra descifrada se obtiene recorriendo desde el final de la palabra hasta el
comienzo, considerando las letras solo en ubicaciones impares. Empezando desde
la última letra. """

def codigo_palabra(codigo):
    return codigo[::-2]
    

print(codigo_palabra("axruatgrrreov"))