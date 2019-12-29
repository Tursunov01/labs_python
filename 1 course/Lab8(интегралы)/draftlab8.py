from math import sin,cos
n1 = int(input('Введите количество разбиения: '))
n2 = int(input('Введите количество 2 разбиения: '))
a = float(input('Введите начальную границу: '))
b = float(input('Введите конечную границу: '))

#задаем функцию
def integral(x):
    return x
#метод прямоугольников
def rectangle(f,xmin,xmax,n):
    delta = (xmax-xmin)/n
    area = 0
    x = xmin
    for i in range(n):
        area += delta * f(x)
        x += delta
    return area
#метод трапеций
def trapezium(f,xmin,xmax,n):
    delta = (xmax-xmin)/n
    area = 0
    x = xmin
    for i in range(n):
        area += delta*(f(x)+f(x+delta))/2
        x += delta
    return area

print ('_____________________________________________________________________')
print ('⏐        Метод       ⏐           n1          ⏐          n2           ⏐')
print ('̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅')
print ('|', 'Прямоугольников   ', '|', '{:20.15f}'.format(rectangle(integral,a,b,n1)), '|', '{:21.15f}'.format(rectangle(integral,a,b,n2)) ,'|')
print('̅' *69)
print ('|', 'Трапеций          ', '|', '{:20.15f}'.format(trapezium(integral,a,b,n1)), '|', '{:21.15f}'.format(trapezium(integral,a,b,n2)) ,'|')
print('̅' *69)



    



