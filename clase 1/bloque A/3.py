#Escriba un programa que invierta un número entero de tres dígitos.
numero = int(input("Ingrese un número: "))
unidad = numero % 10
decena = (numero//10)%10
centena = numero//100
print(str(unidad)+str(decena)+str(centena))