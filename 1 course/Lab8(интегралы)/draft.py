import math

def fn(x):
    return math.sin(x)

#метод прямоугольников
def rect_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*f(x)
        x+=dx
    return area

#метод трапеций
def tr_integral(f,xmin,xmax,n):
    dx=(xmax-xmin)/n
    area=0
    x=xmin
    for i in range(n):
        area+=dx*(f(x)+f(x+dx))/2
        x+=dx
    return area

print("rect_integral = {}".format(rect_integral(fn,1,9,10)))
print("tr_integral = {}".format(tr_integral(fn,1,9,10)))

