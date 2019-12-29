# Задана матрица X(10,8) и массив K(n) (n<=10),
# содержащий номера строк, для которых необходимо определить min элемент.
# Значения min элементов записать в массиве Y.
# Определить среднее значение вычисленных min элеменов.
# Напечатать матрицу Х, массив Y, среднее значение.


m=3   # Количество строк
n=2   # Количество столбцов

print(' Ввод матрицы: ')
x=[[0]*n for i in range (m)]  
for i in range(m):   #10
    for j in range(n):   #8
        print ('Введите элемент № ',j,' строки № ',i)          
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
                print('Введите повторно элемент № ',j,' строки № ',i) 
                a1=(input())
           else:
                 x[i][j]=a1
                 break
print('\nМатрица: ')
for q in x:
  print(q)


k= list(map(int, input('Введите номера строк, в которых необходимо определить min элемент: ').split()))
#k1=int(input('Введите количество строк, в которых необходимо определить min элемент: ')
#for i in range(k1):
 # print ('Введите номер строки: ')
  #a1=input()
 # while True :
 #   k=0
 #   for i in range(len(a1)):                                   
  #    if ('0' < a1[i] <= '9'):
  #        k+=1
  #        
 #   if (k!=len(a1)):
 #        a1=(input('Введите повторно номер строки: '))
  #  else:
  #        kk.append(a1)
  #        break
for i in range(len(k)):
  while k[i]>m :
        k=[]
        k= list(map(int, input('Введите повторно номера строк, в которых необходимо определить min элемент: ').split())) 
       #i=0

y=[0]*len(k)
l=0
h=0
#print(k[h])

#if len(k)>0:

while h < len(k):
 for i in range (m):                                        # Поиск наименьших элементов указанных строк
     #print(i)
     minzn=float(x[i][0])
     #print ('номер строки',i)
     #print('проверяемая строка',k[h])
     if i==k[h]:
        for j in range (n):
        
           if (float(x[i][j])<minzn):
             minzn=float(x[i][j])
        y[l]=minzn
        l+=1
        h+=1
     #else: continue
     if (h==len(k)):
         break

print('Минимальные значения указанных строк: ')
print (y)

s=0
for i in range(len(y)):
    s+=y[i]

srznach=s/len(y)

print( 'Среднее значение вычисленных min элементов= ','{:.4f}'.format(srznach))










