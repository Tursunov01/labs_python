a =[[5,2,3,9],
    [15,6,9,10],
    [25,75,11,14],
    [3,6,20,25]]
##n = int(input('Введите размер матрицы: '))
##for i in range(n):
##    a.append([])
##    for k in range(n):
##        s = int(input('Input number: '))
##        a[i].append(s)
##for q in a:
##    print(q)
        
for i in  range(len(a)-1):
    for j in range (len(a)-1-i):
        summ = 0
        sun=0
        for k in range(len(a)):
            summ += a[k][j]
            sun+= a[k][j+1]
        if (summ > sun):
            for t in range(len(a)):
                a[t][j],a[t][j+1] = a[t][j+1],a[t][j]
        
##count = 0
##coconut = 0
a[0][0] = 0
a[3][3] = 0
for i in range(len(a)):
    for k in range(len(a)):
        if i > k:
            if a[i][k] % 5 == 0:
                a[0][0] += 1
        if i < k:
            if a[i][k] % 5 ==  0:
                a[3][3] += 1
print('ниже диагонали ',a[0][0])
print('выше диагонали ',a[3][3])
for i in a:
    print(i)

