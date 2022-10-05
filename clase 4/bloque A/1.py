""" Desarrolle una función llamada desviacion_estandar(valores) cuyo parámetro
valores sea una lista de números reales. La función debe retornar la desviación estándar
de los valores:
Donde n es la cantidad de valores, 𝑥ҧes el promedio, y los 𝑥𝑖 son cada uno de los
valores. Esto significa que hay que hacerlo siguiendo los siguientes pasos:
1. Calcular el promedio de los valores
2. A cada valor, restarle el promedio, y el resultado elevarlo al cuadrado
3. Sumar todos los valores obtenidos
4. Dividir la suma por la cantidad de valores y sacar la raíz cuadrada del resultado. """

def desviacion_estandar(lista):
    n = len(lista)
    media = sum(lista)/n
    suma = 0
    for num in lista:
        suma += (num - media)**2 / (n -1)
    
    return suma**0.5


lista = [4.0, 1.0, 11.0, 13.0, 2.0, 7.0]

print(desviacion_estandar(lista))