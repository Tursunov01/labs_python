m = int(input("Введите кол-во строк ")) # cтроки
n = int(input("Введите кол-во столбцов  ")) # столбцы

#x = [[int(j) for j in input().split()] for i in range(n)]

x=[[0]*n for i in range (m)]        
for i in range (m):
        for j in range (n):
           x[i][j]=int(input('вв элемент '))
for q in x:
     print(q)

k= int(input('вв номер удаляемой строки '))
for i in range (m):                   #удаление строки
    if (i==k):
        for j in range (n):
           x[i][j]=x[i+1][j]

for i in range (m-1):
        for j in range (n):
           print(x[i][j],end=' ')
        print()




