import random
bukvi = ('q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b','n', 'm')
glasnie = 'eyuioa'
n = int(input('введите длину матрицы: '))
m = int(input('введите ширину матрицы: '))
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        a[i][j] = random.choice(bukvi)
for q in a:
    print(q)
print()

count_max = 0
index_max = 0
bank = 0
for j in range(m):
    summ = ''
    for i in range(n):
        summ += a[i][j]
    for i in glasnie:
        summ = summ.replace(i,'')
    count = len(summ)
    if count == n:
        bank += 1
        if bank == m:
            print('Все столбцы состоят из согласных')
            break

    if count >= count_max:
        count_max = count
        index_max = j
if bank != m:
    for i in range(n):
        a[i] = a[i][:index_max] + a[i][index_max + 1:]
    for q in a:
        print(q)
else:
    print('0')