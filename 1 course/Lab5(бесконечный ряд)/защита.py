x = float(input('Введите значение x: '))
e = float(input('Введите значение точности: '))

t = 1
s = t
l = 1
while abs(t) >= e:
    t = t * x / l
    l += 1
    s += t
print(s)    
