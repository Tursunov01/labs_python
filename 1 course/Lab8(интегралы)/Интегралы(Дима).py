a,b,n1,n2 = map(int,input('Начало,Конец, Кол-во разбиений 1 и 2: ').split())


def f(x):  # Заданная функция
    return x * x


def funs(a,b):  # Первооброзная 
    tfun = (b**3 - a**3) / 3
    return(tfun)


def spr (a,b,n):  # Метод серединных прямоугол.
    h = ( b - a ) / n
    sum = 0
    for i in range(n):
        x = a + h * i + (h / 2)
        sum += f(x)
    I = h * sum
    return(I)

 
def trivos(a,b,n):  # Метод три восьмых  
    h = ( b - a ) / n
    sum1 = 0
    sum2 = 0
    if n % 3 == 0:       
        for i in range (1,n):
            if i % 3 == 0:
                sum1 += f(a + h*i)
            else:
                sum2 += f(a + h*i)
        I1 = (3 / 8) * h * (f(a) + f(b) + 3 * sum2 + 2 * sum1)
    else:
        I1 = 0
    return (I1)
print(" __________________________________________________________________________")                        
print("│           Метод            │{:<10.7g}               │{:<10.7g}".format(n1, n2),"        │")
print("│____________________________│_________________________│___________________│")
print("│Метод серединных прямоугол. │{:<10.7g}               │{:<10.7g}".format(spr(a,b,n1),spr(a,b,n2)),"        │")
print("│____________________________│_________________________│___________________│")
print("│Метод три восьмых           │{:<10.7g}               │{:<10.7g}".format(trivos(a,b,n1),trivos(a,b,n2)),"        │")
print("│____________________________│_________________________│___________________│")
print()
print('Точное значение интегралла:{0:<10.7g}'.format(funs(a,b)))
print()

def otnos(p,tochn):  # Относительная погрешность
    l = (p - tochn) / tochn
    return (l)

print("Относительная погрешность для метода  серединных прямоугол.:")
print("Для n1:","{0:<10.7g}".format(otnos(spr(a,b,n1),funs(a,b))))
print("Для n2:","{0:<10.7g}".format(otnos(spr(a,b,n2),funs(a,b))))
print()
print("Относительная погрешность для метода три восьмых :")
if  trivos(a,b,n1) != 0:
    print("Для n1:","{0:<10.7g}".format(otnos(trivos(a,b,n1),funs(a,b))))
if  trivos(a,b,n2) != 0:
    print("Для n2:","{0:<10.7g}".format(otnos(trivos(a,b,n2),funs(a,b))))
print()


def ab(p,tochn):  # Абсолютная погрешность
    return (p - tochn)

print("Абсолютная погрешность для метода серединных прямоугол.:")
print("Для n1:","{0:<10.7g}".format(ab(spr(a,b,n1),funs(a,b))))
print("Для n2:","{0:<10.7g}".format(ab(spr(a,b,n2),funs(a,b))))
print()

print("Абсолютная погрешность для метода три восьмых:")
if  trivos(a,b,n1) != 0:
    print("Для n1:","{0:<10.7g}".format(ab(trivos(a,b,n1),funs(a,b))))
if  trivos(a,b,n2) != 0:
    print("Для n2:","{0:<10.7g}".format(ab(trivos(a,b,n2),funs(a,b))))
print()


# Определении наименее точного метода(по абсолютной погрешн.) и вычисление его до точности eps

ab1 = ab(spr(a,b,n1),funs(a,b))
ab2 = ab(spr(a,b,n2),funs(a,b))
ab3 = ab(trivos(a,b,n1),funs(a,b))
ab4 = ab(trivos(a,b,n2),funs(a,b))        


eps = float(input('Точность:'))


if trivos(a,b,n2) != 0 or (n2 % 3 == 0) :
    if abs(ab2) < abs(ab4):
        n0 = 3
        while abs(trivos(a,b,(n0*2)) - trivos(a,b,n0)) > eps:
            n0 +=3
        print('Кол-во интераций: ',n0)    
        print("Значение интегралла с заданной точностью"\
              " для метода три восьмых: {0:<10.7g}".format(trivos(a,b,n0)))
    else:
        n0 = 1
        while abs(spr(a,b,(n0*2)) - spr(a,b,n0)) > eps:
            n0 *=2
        print('Кол-во интераций: ',n0)
        print("Значение интегралла с заданной точностью"\
              " для метода середин.прямоугольн.: {0:<10.7g}".format(spr(a,b,n0)))
elif trivos(a,b,n1) != 0 or (n1 % 3 == 0):
    if abs(ab1) < abs(ab3):
        
        n0 = 3
        while abs(trivos(a,b,(n0*2)) - trivos(a,b,n0)) > eps:
            n0 +=3
        print('Кол-во интераций: ',n0)
        print("Значение интегралла с заданной точностью"\
              " для метода три восьмых: {0:<10.7g}".format(trivos(a,b,n0)))
            
    else:
        n0 = 1
        while abs(spr(a,b,(n0*2)) - spr(a,b,n0)) > eps:
            n0 *=2
        print('Кол-во интераций: ',n0)
        print("Значение интегралла с заданной точностью"\
              " для метода середин.прямоугольн.: {0:<10.7g}".format(spr(a,b,n0)))
else:
    print('Среди данных методом невозможно определить наиболее точный')
        
    

