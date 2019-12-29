a = int(input('Введите начальную границу: '))
b = int(input('Введите конечную границу: '))
eps = float(input('Введите значение точности: '))
def f(x):
    return x*x

def method(n):
    h = ( b - a ) / n
    sum1 = 0
    sum2 = 0       
    for i in range (1,n):
        if i % 3 == 0:
            sum1 += f(a + h*i)
        else:
            sum2 += f(a + h*i)
    S = (3 / 8) * h * (f(a) + f(b) + 3 * sum2 + 2 * sum1)
    return (S)
n = 1
I1 = method(n)
I2 = method(2 * n)
n *= 2
while abs(I2 - I1) > eps:
    n *= 2
    I2, I1 = I1, I2
    I2 = method(n)
print("Количество участков разбиения: ", n)
print("Значение определенного интеграла: ",method(n) )
    
        
    
