bn = 7
an = 6
a=[]
b=[]
matrix= []

for i in range(an):
        n = input('Введите {}-ый элемент массива a:'.format(i+1))
        n.strip
        while n.isdigit()==False:
                n = input('Ошибка, введите число еще раз: ')
        n= float(n)
        a.append(n)

for i in range(bn):
        n = input('Введите {}-ый элемент массива b:'.format(i+1))
        n.strip
        while n.isdigit()==False:
                n = input('Ошибка, введите число еще раз: ')
        n= float(n)
        b.append(n)


for i in range(an):
        matrix.append([])
        for k in range(bn):
                s = b[k]*a[i]
                matrix[i].append(s)

for i in range(an):
        print(matrix[i])
i=0
s=0
counter = 0
aritmet1 = 0
for k in range(bn):
        counter = 0
        for i in range(an):
                s+= matrix[i][k]
        aritmet = s/6
        print('Арифметическая стойност {} столбец = {}'.format(k+1,aritmet))
        aritmet1 += aritmet

aritmet2 = aritmet1/7
print('Arifmet stoinost stolbcev = {}'.format(aritmet2))

for i in range (an):
        for k in range(bn):
                if matrix[i][k]>aritmet2:
                        counter +=1

print('kolichestvo = ',counter)
        



