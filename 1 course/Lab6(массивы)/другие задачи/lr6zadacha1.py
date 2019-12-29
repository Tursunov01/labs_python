#Даны 2 одномерных упорядоченных массива
#Сформировать новый упорядоченный массив

#Унтилова Арина ИУ7-16

n1=(input('Введите размер массива №1: '))                      # Ввод размерв массива №1 
while True :
    k=0
    for i in range(len(n1)):                                   
      if ('0' < n1[i] <= '9'):
          k+=1
          
    if (k!=len(n1)):
         n1=(input('Введите повторно размер массива №1: '))
    else:
          break


n2=(input ('Введите размер массива №2: '))                      # Ввод размерв массива №2 
while True :
    k=0
    for i in range(len(n2)):                     
      if ('0' < n2[i] <= '9'):
          k+=1
          
    if (k!=len(n2)):
         n2= (input ('Введите повторно размер массива №2: '))
    else:
          break
        

a=[]
n11=int(n1)
for i in range (n11):
    print('Введите элемент № ',i+1,' первого массива')         #Ввод элементов первого массива
    a1=(input())
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
       k3 = 0
       for m in range (len(a1)-1):
           if ((a1[m]=='e') and (a1[m+1]=='-')) or ((a1[m]=='e') and (a1[m+1]=='+')):
                k3+=1
       if (k3==1):
           k+=2   

       if (k!=len(a1)):
          print('Введите повторно элемент № ',i+1,' первого массива')
          a1=(input())
       else:
         a.append(a1)
         break
        
    
b=[]
n22=int(n2)
for i in range (n22):
    print('Введите элемент № ',i+1,' второго массива')       #Ввод элементов второго массива
    b1=(input())
    while True :
       k2=0
       if b1[0]=='-':
           k=1
       else:
          k=0
        
       for q in range(len(b1)):
         if ('0' <= b1[q] <= '9'):
           k+=1
         if (b1[q]=='.'):
             k2+=1
       if k2==1:
             k+=1

       for m in range (len(a1)-1):
           if ((a1[m]=='e') and (a1[m+1]=='-')) or ((a1[m]=='e') and (a1[m+1]=='+')):
                k3+=1
       if (k3==1):
           k+=2
           
       if (k!=len(b1)):
          print('Введите повторно элемент № ',i+1,' второго массива')
          b1=(input())
       else:
         b.append(b1)
         break

print()
print('Первый массив:')                                  #Вывод массивов
for x in a:
    print(x,end=' ')

print()
print('Второй массив: ')
for x in b:
    print(x,end=' ')

c=[]
x=0


print()
print('Упорядоченный новый массив :')

#for i in range (len(c)-1):                         #Сортировка нового массива методом "пузырька" 
#    for j in range (len(c)-2,i-1,-1):     
#        if float(c[j])>float(c[j+1]):
#            c[j],c[j+1]=c[j+1],c[j]


#c=sorted(c)



с1=['0']*(n11+n22)     
print(c1)
if float(a[0])> float(b[0]):
    c1[0]=(b[0])
    yk1=0
    yk2=1
else:
   c1[0]=(a[0])
   yk1=1
   yk2=0
print (c1)
yk1=0
yk2=0
l=0
while yk1< n11 and yk2 < n22:
    if float(a[yk1]) < float(b[yk2]):
        c1[l]=a[yk1]
        l+=1
        #c1.append(a[yk1])
        yk1+=1
    
    else:
         c1[l]=b[yk2]
         l+=1
         #c1.append(b[yk2])
         yk2+=1

if (yk1< n11):
    for i in range (yk1,n11+1):
        c1[l]=a[yk1]
        l+=1
        #c1.append(a[yk1]) 

else:
     for i in range (yk2,n22+1):
        c1[l]=b[yk2]
        l+=1
        # c1.append(b[yk2])
    
        
print(c1)

    

    
    
    
 
  

