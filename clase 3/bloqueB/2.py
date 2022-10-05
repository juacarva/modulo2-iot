""" A cada cadena le corresponde una cadena complementaria, que se obtiene
intercambiando las adeninas con las timinas, y las citosinas con las guaninas.
cadena = ‘cagcccatgaggcagggtg’
complemento = ‘gtcgggtactccgtcccac’
Escriba la función complementaria(c) que entregue la cadena complementaria
de c. """

def complementaria(cadena):
    comp = ''
    for letra in cadena:
        if letra == 'a':
            comp += 't'
        elif letra == 't':
            comp += 'a'
        elif letra == 'c':
            comp += 'g'
        else:
            comp += 'c'
    return comp

print(complementaria('cagcccatgaggcagggtg'))
