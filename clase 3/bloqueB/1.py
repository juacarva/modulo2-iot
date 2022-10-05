""" Una cadena de ADN es una secuencia de bases nitrogenadas llamadas: (1) adenina, (2) citosina, (3) timina y
(4) guanina. En un programa una cadena se representa como un string de caracteres ‘a’, ‘c’, ‘t’ y ‘g’. Escriba
la función cadena_al_azar(n) que retorne una cadena aleatoria de ADN de largo n. """

from random import randint

def cadena_al_azar(n):
    caracteres = "actg"
    cadena = ''
    i = 0
    while i < n:
        cadena = cadena + caracteres[randint(0,3)]
        i += 1
        
    return cadena

print(cadena_al_azar(5))
