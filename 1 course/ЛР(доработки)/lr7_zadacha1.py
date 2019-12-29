# Определить min элемент в каждой строке матрицы D(M,N),
# запомнить их в массиве G.
# В массиве G поменять местами первый и последний положительные элементы.

# Унтилова Арина ИУ7-16Б

M1=(input('Введите количество строк матрицы: '))                 
while True :
    k=0
    for i in range(len(M1)):                                   
      if ('0' < M1[i] <= '9'):
          k+=1
          
    if (k!=len(M1)):
         M1=(input('Введите повторно количество строк матрицы:: '))
    else:
          break
N1=(input('Введите  количество столбцов матрицы: '))        
while True :
    k=0
    for i in range(len(N1)):                                   
      if ('0' < N1[i] <= '9'):
          k+=1
          
    if (k!=len(N1)):
         N1=(input('Введите повторно количество столбцов матрицы: '))
    else:
          break
N=int(N1)
M=int(M1)
D=[[0]*N for i in range (M)]                                    # Ввод элементов матрицы
for i in range (M):
    for j in range (N):
        print ('Введите элемент № ',j+1,' строки № ',i+1)          
        a1=(input())
        k3=0
        while True :
           k2=0
           if a1[0]=='-':
             k=1
           else:
             k=0
           for q in range(len(a1)):
             if ('0' <= (a1[q]) <= '9'):
               k+=1
             if (a1[q]=='.'):
                k2+=1
           if k2==1:
                k+=1
           for m in range (len(a1)-1):
             if ((a1[m]=='e') and (a1[m+1]=='-')) or ((a1[m]=='e') and (a1[m+1]=='+')):
                k3+=1
           if (k3==1):
                k+=2   

           if (k!=len(a1)):
                print('Введите повторно элемент № ',j+1,' строки № ',i+1) 
                a1=(input())
           else:
                 D[i][j]=a1
                 break
       
print('\nНачальная матрица:')
for q in D:
    print (q)

G=[0]*M
l=0

for i in range (M):                                        # Поиск наименьших элементов каждой строки
    minzn=D[i][0]  
    for j in range (N):
        if (D[i][j]<minzn):
            minzn=D[i][j]
    G[l]=minzn
    l+=1

print('\nНачальный массив G: ')
print(G)

k=0
for i in range (M):
    if float(G[i])>0:
        k+=1
if(k==0):
    print ('\nВ массиве G нет положительных элементов')
else:
    for i1 in range (M):                                # Запоминание номера первого положительного элемента массива
      if float(G[i1])>0:
         n1=i1
         break
         
    for i2 in range (M):                                # Запоминание номера последнего положительного элемента массива
      if float(G[i2])>0:
         n2=i2
    G[n1],G[n2]=G[n2],G[n1]
    print('\nПреобразованный массив G: ')
    print (G)

    
        

