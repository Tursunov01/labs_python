m=int(input('количество строк/cтолбцов матрицы: '))
#n=int(input('количество столбцов матрицы: '))

x=[[0]*m for i in range(m)]
#print (x)
for i in range(m):
    for j in range(m):
        print ('Введите элемент матрицы: ')
        x[i][j]=float(input())

for q in x:
    print(q)
print()
for i in range(len(x)):
    for j in range (i+1):
      print (x[i][j],end=' ')
    print()
print()
for i in range( len(x)):
    print(' '*(m+i),end=' ')
    for j in range (i,len(x)):
      print (x[i][j],end=' ' )
    print (' '*(m+i))
      
print()


        
