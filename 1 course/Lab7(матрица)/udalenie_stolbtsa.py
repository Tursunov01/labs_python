'''m = int(input("Введите кол-во строк ")) # cтроки
n = int(input("Введите кол-во столбцов  ")) # столбцы


x=[[0]*n for i in range (m)]        
for i in range (m):
        for j in range (n):
           x[i][j]=int(input('вв элемент '))
for q in x:
     print(q)

k= int(input('вв номер удаляемого столбца '))
for i in range (m):                                   #удаление столбца
    for j in range (n):
            if (j-1==k):
               x[i][j]=x[i][j+1]

for i in range (m):
        for j in range (n-1):
           print(x[i][j],end=' ')
        print()
'''
n = int(input(''))
m = int(input())
a = [[1 for j in range(n)] for i in range(m)]
count = 1
col = -1
for i in range(m):
    if i % 2 == 0:
        for j in range(n):
            a[m - i - 1][j] = count
            if count == 8: col = j
            count += 1


    else:
        for j in range(n - 1, -1, -1):
            a[m - i - 1][j] = count
            if count == 8: col = j
            count += 1

for i in a:
    print(i)
print()
if col > -1:
    for i in range(len(a)):
        a[i].pop(col)

for i in a:
    print(i)