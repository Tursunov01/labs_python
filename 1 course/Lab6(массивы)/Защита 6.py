N = int(input('Введите количество элементов: '))
b = [i for i in range(N)]
count = 0
count1 = N-1
for i in range(N):
    a = float(input('Введите элемент №' + str(i+1) + ' массива: '))
    if a % 2 == 1:
        b[count] = a
        count +=1
    if a % 2 == 0:
        b[count1] = a
        count1-=1
print(b)
c = 0
for k in range(len(b)):
    if b[k] < 0:
        c += 1
    elif c > 0:
         b[k-c] = b[k]
print(b[:N-c])

