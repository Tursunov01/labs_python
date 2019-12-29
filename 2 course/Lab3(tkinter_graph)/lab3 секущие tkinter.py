from tkinter import *
from math import *
from tkinter.messagebox import *
import matplotlib.pyplot as plt
import numpy as np
NMAX = 1000
def f(x):
    return cos(x)-x+1
    #return x*x-4
    #return sin(x)
def name():
    #return 'x^2 -4'
    return 'sin(x)'
    #return 'x-cos(x)'
def f2(x):
    return -sin(x)

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
        
def perevod(stri):
    if ',' in stri:
        if stri[0]=='-':  #перевод отрицательного вещественного числа
            k = stri.find(',')
            celay = int(stri[1:k])
            drobnay=stri[k+1:]
            p=int('1'+'0'*len(drobnay))
            d = int(drobnay)
            d = d/p
            c = celay+d
            c = c *(-1)
            return c
        else:
            k = stri.find(',')
            celay = int(stri[:k])
            drobnay=stri[k+1:]
            p=int('1'+'0'*len(drobnay))
            d = int(drobnay)
            d = d/p
            c= celay+d
            c = c *(-1)
            return c
    else:
        return int(stri)
def clean():
    box.delete(0,END)
def dannye():
    x1 = float(a.get())
    x2 = float(b.get())
    H = float(h.get())        
    epsilon = float(eps.get())
    itere = int(maxit.get())
    return x1,x2,epsilon,H,itere
def grafik(start,end,epsil):
    step = 0.001
    if abs(f(end)) < epsil:
        end += 1
    x = np.arange(start, end, step)
    y = []
    for i in x:
        y.append(f(i))
    fig = plt.figure()
    plt.plot(x, y)    # ломаная линия;
    for i in x:
        if (abs(f(i)) <= 0.01):
            plt.scatter(i, f(i), c='r')
        if (abs(f2(i)) <= 0.01):
            plt.scatter(i,f2(i), c = 'b')
    plt.title('График функции ' +name() +'\n красные - корни' + '\n синие - точки перегиба')
    plt.ylabel('f(x)')
    plt.xlabel('x')
    plt.grid(True) 
    plt.show()
def raschet():
    clean()
    m = []
    korni=[]
    x1,x2,epsilon,h, itere = dannye()
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
               text = " "*5 + l+"     " +" "*20 + a+"    "+ b+" "*18+" "*9+x +10*" "+f1+" "+20*" "+ d +5*" "
               m.append(text) #массив содержащий информацию о корнях
               n = n + 1
        k = k+h
    n = 1
    for i in range(len(m)):
        box.insert(END,m[i])
    grafik(w,z,1e-5)
root = Tk()
root.title('Казакова лаб.№3')
root.geometry('700x600') #расширение экрана

t1=Label(text='Уточнение корней методом секущих',font = 'Arial')
t1.pack()

alabel = Label(text = 'Введите нижнюю границу')
alabel.pack(side=LEFT)
alabel.place(x = 20,y = 25)
a = Entry(width=30)  #полевводанижнейграницы
a.place(x=100,y=50)
a.pack()

box = Listbox(width = 100, height = 10)
box.place(x = 50, y = 190)

blabel = Label(text = 'Введите верхнюю границу')
blabel.pack(side=LEFT)
blabel.place(x = 20,y = 45)
b = Entry(width=30)   #полеввода верхней границы
b.place(x = 100, y = 150)
b.pack()

hlabel = Label(text = 'Введите шаг')
hlabel.pack(side=LEFT)
hlabel.place(x = 20,y = 65)
h = Entry(width=30)  #полевводашага
h.place(x=100,y=250)
h.pack()

epslabel = Label(text = 'Введите точность')
epslabel.pack(side=LEFT)
epslabel.place(x = 20,y = 85)
eps = Entry(width=30)   #полевводаэпсилон
eps.place(x = 100, y = 350)
eps.pack()

maxitlabel = Label(text = 'Введите кол-во итераций')
maxitlabel.pack(side=LEFT)
maxitlabel.place(x = 20,y = 105)
maxit = Entry(width=30)   #полевводаэпсилон
maxit.place(x = 100, y = 450)
maxit.pack()

raschet = Button(root,text = 'Рассчитать', command = raschet, font = 'Arial 8' )
raschet.place(x = 290,y = 140)

N= Label(text = "№ "+"|"+" "*10+"границы"+" "*10+"|"+" "*7+" x      "+ "|"+10*" "+" f(x)     "+"|"+5*" "+"кол-во итераций  "+"|",font = 'Arial 10')
N.place(x=10,y=170,width = 600,height=20)

'''def secante(f, x0, x1, tol, maxit):
    fx0 = f(x0)
    fx1 = f(x1)
    q,w = x0,x1
    for i in range(3,maxit):
        if abs(fx1) < tol:
            return x1,i
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        if not (x0 < x2 < x1):
            return secante(f,x0-0.1,x1,tol,maxit)
        x0,  x1  = x1,  x2
        fx0, fx1 = fx1, f(x2)'''
