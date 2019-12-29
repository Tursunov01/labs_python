'''#4
N = int(input('Введите количество элементов: '))
b = []
for i in range(N):
    a = float(input('Введите элемент: '))
    b.append(a)
for k in range(len(b)-1, -1, -1):
   print(b[k], end=' ')'''

#5
N = int(input('Введите количество элементов: '))
b = []
for i in range(N):
    a = float(input('Введите элемент: '))
    if i % 2 == 0:
        b.append(a)
for k in range(N-1,-1,-1):
    a = float(input('Введите элемент: '))
    if a % 2 == 1:
        b.append(a)
print(b)

