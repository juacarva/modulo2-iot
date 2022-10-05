""" Escriba un programa que resuelva una ecuación de segundo grado de la
forma:

Recuerde que primero debe calcular el discriminante (d=b**2–4*a*c)
para determinar si la ecuación, (1) no tiene solución real (d<0), (2) tiene
solución única (d==0) o (3) tiene 2 soluciones (d>0). """

def discriminante(a, b, c):
    return b**2 - 4*a*c

def ecuacion2(a,b,c):
    if discriminante(a,b,c) < 0:
        return "La ecuación no tiene solución"
    elif discriminante(a,b,c) == 0:
        return "Sol: " + str(round((-b / (2*a)),2))
    else:
        return "sol_1 = " + str(round((-b + discriminante(a,b,c)**(1/2))/(2*a),2)) + ", Sol_2 = " + str(round((-b - discriminante(a,b,c)**(1/2))/(2*a),2))

a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))

print(ecuacion2(a,b,c))
