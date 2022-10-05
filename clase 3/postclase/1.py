""" Escriba un programa que lea una cantidad de palabras y calcule el largo de
cada una, sin considerar las letras repetidas, determinando la más larga
y más corta. Por ejemplo, la palabra “casa” es más corta que la palabra
“reno”, ya que tiene 3 letras distintas (c, a y s). Mientras que “reno” tiene 5. """

def cuenta_letras(palabra):
    letras = ""
    for letra in palabra:
        if letra not in letras:
            letras = letras + letra
    return len(letras)

n = int(input("Ingrese n: "))

max = -float('inf')
min = float('inf')
palabra_larga = ""
palabra_corta = ""

i = 1
while i <= n:
    palabra = input("palabra " + str(i) +" :")
    letras = cuenta_letras(palabra)
    if letras > max:
        max = letras
        palabra_larga = palabra
    if letras < min:
        min = letras
        palabra_corta = palabra
    i += 1

print("la palabra más larga es: ", palabra_larga)
print("la palabra más corta es: ", palabra_corta)