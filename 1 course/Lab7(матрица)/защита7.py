n = int(input('Введите размер квадратной матрицы: '))
m = int(input('Введите число: '))
##j = n - 1
a = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for k in range(n-i):
            a[k][n-k-1-i] = m
            if  k >= -k-1-i:
                m += 1
for i in range(n):
    print(a[i])
