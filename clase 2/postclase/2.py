""" El banco CBI necesita implementar mejoras en sus mecanismos de seguridad, precisamente en los
que están relacionados con la generación de claves iniciales para sus clientes de tarjetas de crédito.
Para esto, desarrolle un programa que permita generar una clave de 4 dígitos, usando el siguiente
algoritmo:

• Leer tantos números como sea necesario para generar la clave.

• Para cada número deberá recorrer su dígitos y encontrar el menor.

• Si el dígito menor es par, pasará a formar parte de la clave, en caso contrario, se procesa el
siguiente número hasta formar la clave de 4 dígitos.

• Mostrar la clave obtenida. """

clave = ""
while len(clave) < 4:
    nro = int(input("Ingrese un número entero: "))
    digito_menor = float('inf')
    while nro > 0:
        digito = nro % 10
        if digito < digito_menor:
            digito_menor = digito
        nro = nro // 10
    if digito_menor % 2 == 0:
        clave += str(digito_menor)

print(clave)