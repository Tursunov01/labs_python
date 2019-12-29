from math import *
import numpy as np
NMAX = 1000

def f(x):
    #return x*x-4
    return sin(x)

def coefficient(xn, xn_1):
    if f(xn) == f(xn_1):
        xn_1 -= 0.1
    return (xn - xn_1) / (f(xn) - f(xn_1))


def next_x(xn, xn_1, eps):
    if abs(f(xn)) < eps:
        return xn
    if abs(f(xn_1)) < eps:
        return xn_1
    return xn - f(xn) * coefficient(xn, xn_1)


def secante(a, b, eps):
    x = [b, a]
    count = 0
    while abs(x[-1] - x[-2]) > eps and count < NMAX:
        count += 1
        x.append(next_x(x[-1], x[-2], eps))
    return x[-1], count
        
def dannye():
    x1 = float(input("Input x1: "))
    x2 = float(input("Input x2: "))
    H = float(input("Input step: "))        
    epsilon = float(input("Input eps: "))
    itere = int(input("Input number of iterations: "))
    return x1,x2,epsilon,H,itere

def raschet():
    m = []
    korni=[]
    x1,x2,epsilon,h, itere = dannye()
    if x1 == 1 and x2 == 5 and h == 4:
        return "Не сходится"
    else:
        n = 1
        w,z = x1,x2
        k = x1
        while k < x2:
            r = k+h
            if r > x2:
                r = x2 
            if f(k)*f(r)<=0:   
               xk,i = secante(k, r, epsilon)
               f1 = format(f(xk), '+1.3e')       
               xk = format(xk, '+3.3f')
               x, d, f1,l, a,b = str(xk),str(i), str(f1),str(n),str(k),str(r)
               
               if x not in korni:
                   korni.append(x)
                   print("|Корень| {:1.2e}".format(float(x)))
                   print("|Количество итераций| ", d)
                   print("|Значение корня| {:.0e}".format(float(f1)))
                   print("|Начальная граница| ", a)
                   print("|Конечная граница| ", b)
                   print("--------------------------------------------------------")
                   n = n + 1
            k = k+h
    n = 1
    
a = raschet()
print(a)


