a = int(input('Введите начальную границу: '))
b = int(input('Введите конечную границу: '))
E = float(input('введите эпсилон = '))

def f(x):
    return x
def Ip(s,n,m,f):
    I = f(a)+ f(b)
    if m%2==1:
      m = m+1
    h = (n-s)/(m)
    x = a+h
    for i in range(1,m):
          if i%2==0:
              I+=f(x)*2
          else:
              I+=f(x)*4
          x+=h
    I*=h
    I/=3
    I*=sign
    return I
n = 1
I1 = Ipr(a,b,1,f)
I2 = Ipr(a,b,2,f)
while abs(I2-I1)>E:
    I2 = Ipr(a,b,n,f)
    n*=2
    I1 = I2
    I2 = Ipr(a,b,n,f)
    if abs(I2-I1) < E:
        print(n)
        break
print('наиболее точный результат',I2)
