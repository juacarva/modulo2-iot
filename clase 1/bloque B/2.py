""" Escriba un programa que pida al usuario dos palabras, e indique cual
de ellas es la más larga, y por cuantas letras lo es. """

p1 = input("Ingrese palabra 1: ")
p2 = input("Ingrese palabra 2: ")

if len(p1)==len(p2):
    print("Ambas palabras tienen el mismo largo")
elif len(p1)>len(p2):
    print(p1, "es mayor que", p2, "por", len(p1)-len(p2), "letra(s)")
else:
    print(p2, "es mayor que", p1, "por", len(p2)-len(p1), "letra(s)")