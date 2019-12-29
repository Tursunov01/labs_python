#Александър Чаушев
#ИУ7 - 16Б
#Масив лаб 6
n = input('Введите размер массива')
n.strip()       
while n.strip('-').replace('.','',1).replace('e-','',1).replace('e-','',1).isdigit() == False:
        n = input('Ошибка, введите число еще раз: ')
n = int(float(n))
array = [0]*n
if len(array) <= 0:
        print('размер масива 0')
else:
        for i in range(n):
                m = input('Введите элемент {}-ый массива: '.format(i+1))
                m.strip()
                while m.strip('-').replace('.','',1).replace('e-','',1).replace('e-','',1).replace('e+','',1).isdigit() == False:  #Проверка ввода
                        m = input('Ошибка, введите число еще раз: ')
                chislo1 = ''
                chislo2 = ''
                summa = 0
                print('razmer',len(m))
                for k in range(len(m)):
                        print('--->{} ->>>{}'.format(k,m[k]))
                        if m[k] == 'e':
                                if m[k+1] == '-':
                                        znak = 'minus'
                                else:
                                        znak = 'plus'
                                
                                for p in range(k):
                                        chislo1 += m[p]
                                        chislo1 = float(chislo1)
                                        if k < len(m):
                                                for z in range (k+1,len(m)):
                                                        chislo2+=m[z]
                                                        chislo2 = float(chislo2)
                                #1e-5.3
                        print('chislo1',chislo1)
                        print('chislo2',chislo2)
                        if m[k]== 'e':
                                if znak == 'minus':
                                        summa = chislo1*(10**(chislo2))
                                else:
                                        summa = chislo1*(10**(chislo2))

                        print(summa)
                        n = summa
        array.append(n)
        print('Ваш массив:',array)
        length = len(array)
        array1 
        output = array[0]
        for i in range(1,length):
            if array[i]>array[0]:   #Условие
                output = array[i]
        if output == array[0]:
            print('Нету такого элемента')
        else:
            print('Последный элемент который удоволетворяет условию X > A[0]: ',output)
        for k in range(length):
            s = 0  #сумма делителей
            for z in range(1,int(float(array[k]))):
                if array[k]%z == 0:
                    s += z
            if s-array[k]==0 and array[k] != 0:  #Совершенние числа
                array1.append(array[k])
        print('Совершенние числа:',array1)
        
