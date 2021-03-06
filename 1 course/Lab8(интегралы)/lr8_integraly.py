# Вычисление определенного интеграла методом 3/8 и
# серединных прямоугольников.

# Унтилова Арина ИУ7-16
from math import sin,cos
def f(x):
    #return x*x*x
    return x*x

def sred_pr(n):                          # Вычисление определенного интеграла методом серединных прямоугольников 
    h = (b - a) / n
    s = 0
    x = a + h/2
    for i in range(1, n+1):
        s += f(x)
        x += h
    I = h * s
    return I

def method3_8(n):                        # Вычисление определенного интеграла методом 3/8
    n = n // 3
    n = n * 3
    S = f(a) - f(b)
    h = (b - a) / n
    x = b
    while n > 2:
      S = S + 3 * (f(x - 2 * h) + f(x - h)) + 2 * (f(x))
      n = n - 3
      x = x - 3 * h

    S = S * 3 * h / 8
    return S




def printf(a):
    
                                                           # вывод значений
    if (abs(a) < 0.00001) or (abs(a) > 10000):             
        s = "{:.8}".format(a)
    else:
        s = "{:9.8f}".format(a)
        
    s = "{:9.8f}".format(a)
    s = s + " " * (11 - len(s))
    return s
print("Данная программа вычисляет определенный интеграл")
print("с помощью методов 3/8 и серединных прямоугольников:")
print("Введите данные через пробел: ")

a, b = map(float, input("Введите а и b: ").split())
n1, n2 = map(int, input("Введите n1 и n2 (количество участков разбиения): ").split())

print("|-------------------------------------------------------|")
print("|     Метод       |       n1          |       n2        |")
print("|-------------------------------------------------------|")

I1 = sred_pr(n1)
I2 = sred_pr(n2)

print("|  Ср. прямоуг.   |", printf(I1), "    |", printf(I2), "  |")
print("|-------------------------------------------------------|")

I1 = method3_8(n1)
I2 = method3_8(n2)

print("|       3/8       |", printf(I1), "    |", printf(I2), "  |")
print("|-------------------------------------------------------|")

print("Вычисление с точностью eps методом серединных прямоугольников:") 
eps = float(input("Введите точность вычислений eps = "))                #Вычисление с точностью eps методом серединных прямоугольников
n = 1
I1 = sred_pr(n)
I2 = sred_pr(2 * n)
n *= 2
while abs(I2 - I1) > eps:
    n *= 2
    I2, I1 = I1, I2
    I2 =sred_pr(n)
print("Количество участков разбиения: ", n)
print("Значение определенного интеграла: ", printf(I2))
