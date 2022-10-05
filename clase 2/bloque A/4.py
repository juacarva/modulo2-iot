""" Un viajero desea saber cuánto tiempo tomó el viaje que realizó. Él tiene la duración
en minutos de cada uno de los tramos del viaje.
Escriba un programa que permita ingresar los tiempos de viaje de los tramos y
entregue como resultado, el tiempo total de viaje en formato horas:minutos .

El programa debe dejar de pedir tiempos cuando se ingrese un 0. """

tiempo = 1
total = 0
while tiempo != 0:
    tiempo = int(input("Ingrese el tiempo del tramo (0 para terminar): "))
    total = total + tiempo

horas = total // 60
minutos = total % 60

print("Tiempo total de viaje: " + str(horas)+":"+str(minutos)+" horas")