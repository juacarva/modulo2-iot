""" Las funciones seno y coseno, pueden ser representadas por sumas infinitas:
1) Escriba la función factorial_reciproco(n), que retorne el valor de 1/n!
2) Escriba la función signo(n) que retorne 1 cuando n es par, y -1 cuando n
es impar.
3) Escriba las funciones seno_aprox(x, m) y coseno_aprox(x, m) que
aproximen el seno y el coseno de x, usando los primeros m términos de las
sumatorias. """

from math import factorial, pi, sin

def factorial_reciproco(n):
    i = 1
    factorial = 1
    while i <= n:
        factorial *= i
        i += 1
    return 1/factorial

def signo(n):
    if n%2 == 0:
        return 1
    return -1

def seno_aprox(x,m):
    i = 1
    j = 1
    seno = 0
    while i <= m:
        seno = seno + (x**j) * factorial_reciproco(j) * signo(i+1)
        i += 1
        j += 2
    return seno

def coseno_aprox(x,m):
    i = 0
    j = 1
    coseno = 0
    while i < m:
        coseno = coseno - (x**(j-1)) * factorial_reciproco(j-1) * signo(i+1)
        i += 1
        j += 2
    return coseno
        

a = pi - pi**3/factorial(3) + pi**5/factorial(5) - pi**7/factorial(7)
print(a)
print(seno_aprox(pi,4))

b = 1 - pi**2/factorial(2) + pi**4/factorial(4)# - pi**6/factorial(6)
print(b)
print(coseno_aprox(pi,3))

