n = int(input('Введите размер массива: '))
array = [0]*n
if len(array) <= 0:
        print('размер масива 0')        
else:
        for i in range(n):
                array[i] = input('Введите элемент {}-ый массива: '.format(i+1))
                array[i].strip()
                while array[i].isdigit() == False:  #Проверка ввода
                        array[i] = input('Ошибка, введите число еще раз: ')
                array[i] = int(array[i])
print('Ваш массив:',array)
c=0
x=1
counter = 0
for i in range(n):
    n_max = n-c
    if i<n_max and array[i]%2==0:
       if array[i+1]%2==0:
               u = i+2
               x = 1
               counter +=1
               print('counter',counter)
               for k in range(u,len(array)):
                       array[i+x] = array[k]
                       x+=1
                       print('k',k)
               array[len(array)-1] = 1
       c +=1
           
print('Ваш массив:',array[0:len(array)-counter])

