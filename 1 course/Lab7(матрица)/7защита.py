n = int(input('Введите количество столбцов: '))
m = int(input('Введите количество строк: '))
a = [[1 for j in range(n)]for i in range(m)]
count = 1
col = -1
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            a[m-i-1][j] = count
            if count == 8:
                col = j
            count += 1
    else:
        for j in range(n-1, -1, -1):
            a[m-i-1][j] = count
            if count == 8:
                col = j
            count += 1
for i in a:
    print(i)
print()
if col > -1:
    for i in range(len(a)):
        a[i].pop(col)
for i in a:
    print(i)
