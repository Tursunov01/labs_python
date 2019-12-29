n = 6
v = []
while True:
    try:
        m = int(input('Введите цифру: '))
    except ValueError:
        print(' введите заного')
        continue
    else:
        break
m = float(m)
a = [[0]*n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
        elif i > j:
            a[i][j] = 1
        elif i < j:
            a[i][j] = m
            m += 1
for t in a:
    print(t)
for i in range(n):
    s = 0
    for j in range(n):
        s += a[i][j]
        v.append(s/6)
print('Наибольшше значение строки:= ' '{:0.2f}'.format(max(v)))
