
from math import sin,cos
while True:
    try:
        n1 = int(input('Введите количество 1 разбиения: '))
        if n1 <= 0:
            print(' введите размер заново')
            continue
    except ValueError:
        print(' введите размер заново')
        continue
    else:
        break
while True:
    try:
        n2 = int(input('Введите количество 2 разбиения: '))
        if n2 <= 0:
            print(' введите размер заново')
            continue
    except ValueError:
        print(' введите размер заново')
        continue
    else:
        break
while True:
    try:
        a = float(input('Введите начальную границу: '))
    except ValueError:
        print(' введите размер заново')
        continue
    else:
        break
while True:
    try:
        b = float(input('Введите конечную границу: '))
    except ValueError:
        print(' введите размер заново')
        continue
    else:
        break
#задаем функцию
def integral(x):
    return x*x
##метод прямоугольников
def rectangle(n):
    delta = (b-a)/n
    area = 0
    x = a
    for i in range(n):
        area += delta * integral(x)
        x += delta
    return area
#метод трапеций
def trapezium(n):
    delta = (b-a)/n
    area = 0
    x = a
    for i in range(n):
        area += delta*(integral(x)+integral(x+delta))/2
        x += delta
    return area
print ('_____________________________________________________________________')
print ('⏐        Метод       ⏐           n1          ⏐          n2           ⏐')
print ('̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅')
print ('|', 'Прямоугольников   ', '|', '{:20.15f}'.format(rectangle(n1)), '|', '{:21.15f}'.format(rectangle(n2)) ,'|')
print ('̅' *69)
print ('|', 'Трапеций          ', '|', '{:20.15f}'.format(trapezium(n1)), '|', '{:21.15f}'.format(trapezium(n2)) ,'|')
print ('̅' *69)
print ("Вычисление с точностью eps методом трапеций:") 
while True:
    try:
        eps = float(input("Введите точность вычислений eps = ")) 
    except ValueError:
        print(' введите размер заново')
        continue
    else:
        break                           #Вычисление с точностью eps методом трапеций
n = 1
I1 = trapezium(n)
I2 = trapezium(2*n)
n *= 2
while abs(I2 - I1) > eps:
    n *= 2
    I2, I1 = I1, I2
    I2 =trapezium(n)
print("Количество участков разбиения: ", n)
print("Значение определенного интеграла: ", integral(I2))


    



