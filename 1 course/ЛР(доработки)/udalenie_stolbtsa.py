m = int(input("Введите кол-во строк ")) # cтроки
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
            if (j==k):
               x[i][j]=x[i][j+1]

'for i in range (m):
        for j in range (n-1):
           print(x[i][j],end=' ')
        print()
