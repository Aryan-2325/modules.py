import math
#NOTE:This file is meant to be imported not run directly
#----------------------------------------------------------------------------------------------------------------------#
#Quadratic equation ---> ax^2 + bx + c = 0
def quadratic(a,b,c):
    del1 = (b ** 2) + (-4 * (a * c))
    del2 = math.sqrt(del1)
    x1 = (-b + del2) / (2 * a)
    x2 = (-b - del2) / (2 * a)
    return x1,x2

#facotrial
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

#coverting cel to far and vice versa
def c_f(C):
    far = (C * 1.8) + 32
    far2 =round(far)
    ans = (f'{far2}°F')
    return ans

def f_c(F):
    cel = (F - 32) / 1.8
    cel2 =round(cel)
    ans = (f'{cel2}°C')
    return ans

#Kelvin to cel and vice versa
def c_k(c):
    k = c + 273
    return f'{k}°K'

def k_c (T):
    c = T - 273
    return f'{c}°C'

#Tarkib ---> C(n,r) = n! / r!(n-r)!
def C(n,r):
    m = n - r
    cn = (factorial(n)) / (factorial(r) * factorial(m) )
    return cn

#Jaigasht ---> P(n,r) = n! / (n-r)!
def P(n,r):
    m = n - r
    pn = (factorial(n)) / factorial(m)
    return pn

#Fibonacci sum
def fib(n):
    m = 0
    for i in range(1,n + 1):
        m = i + m
    return m































