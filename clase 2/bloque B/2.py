""" En estadística descriptiva, se define el rango de un conjunto de datos reales
como la diferencia entre el mayor y el menor de los datos.

Por ejemplo, si los datos son [5.96, 6.74, 7.43, 4.99, 7.20, 0.56,
2.80] entonces el rango será: 7.43 – 0.56 = 6.87

Escriba un programa que; (1) pregunte al usuario cuántos datos ingresará, (2)
pida los datos uno por uno y (3) entregue como resultado el rango de los
datos (suponga que todos los datos que ingrese serán válidos). """

n = float(input("Cantidad de números: "))

mayor = -float('inf')
menor = float('inf')
i = 0
while i < n:
    nro = float(input("Ingrese numero "+ str(i+1)+": "))
    if nro > mayor:
        mayor = nro
    if nro < menor:
        menor = nro
    i += 1
print("El rango de los datos es: ",round(mayor - menor,1))