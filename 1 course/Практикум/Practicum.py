#Учебно-Вычислительный практикум
#Сканер
#Турсунов Жасурбек
#ИУ7-16Б
#25.12.2018

'''a = [  [10,10,6,4,6,8,13,15,11,6,],
	  [0,1,2,2,2,2,4,5,5,6,7,6,5,6,6,5,5,6,6,3,2,2,1,0,],
	  [2,4,5,5,7,6,7,10,10,10,7,3,3,5,5,],                      #Исходные данные(Ввод)
	  [0,0,0,0,2,4,4,6,9,9,8,8,7,5,4,3,4,4,4,4,3,1,0,0,],
        ]'''
a = [	[3,3,2,2,4,3,],
	[1,0,1,1,3,1,2,1,2,3,0,1,1],         #Для проверки
	[2,2,2,2,2,2,2,3],
	[0,0,2,2,2,3,1,2,2,1,0,2,0,]
      ]
'''a = [  [3,3,5,6,2,],
	  [0,1,2,2,3,3,2,3,2,1,0,],      #Для проверки
	  [0,4,4,3,5,2,1,],
	  [0,0,1,3,3,4,4,3,1,0,0,]
	]'''

def output(arr):
	for i in arr:
		for j in i:
			if j == 0: print('.', end = ' ')      #Если поппадается часть объекта, то ставим "#", в противном случае "."
			else: print('#', end = ' ')
		print()

def checkmax(i, j):
	boo = (c[0][i] == n) or  (c[2][j] == m)
	if boo:                                           
		return True	
	if (i + j) <= m - 1:                          
		boo = (c[1][i + j] == i + j + 1)
	elif (i + j) >= n - 1:
		boo = (c[1][i + j] == m + n - (i + j + 1))
	else :
		boo = (c[1][i + j] == m)
	if boo: return boo


	
	if (i - j + n - 1) <= m - 1:
		boo = c[3][i - j + n - 1] == i - j + n
	elif (i - j + n - 1) >= n - 1:
		boo = c[3][i - j + n - 1] == m + n - (i - j + n)    
	return boo

def check(i,j):
	return (a[0][i] > 0) and (a[2][j] > 0) and (a[1][i + j] > 0) and (a[3][i - j + n - 1] > 0) 

def select(i,j):
	global count, a, result, count0, n, m, find        #Глобальные переменные для использования их в программе
	if j > n - 1: 
		i += 1
		j = 0	
	if count == 0:
		output(result)
		find = True
		return None

	elif (i <= m - 1) and ((n * (m - 1 - i) + (n - j)) >= count) and (not find) :     #2 скобка считает количество ячеек после точки,
                                                                                          #1 скобка чтобы не переходила на следующую строчку
		# not select cell (i,j)
		if (not (checkmax(i, j))) and (count0 > 0):
			count0 -= 1  
			result[i][j] = 0                                  #Счетчик count0 считает количество нулей
			select(i, j + 1)
			count0 += 1
		if (check(i, j) and count > 0) and (not find) :
		#select cell (i,j)
			result[i][j] = 1
			count -= 1
			a[0][i] -= 1
			a[2][j] -= 1
			a[1][i + j] -= 1
			a[3][i - j + n - 1] -= 1	#Счетчик count считает количество единиц
			select(i, j + 1)	
			result[i][j] = 0
			count += 1
			a[0][i] += 1
			a[2][j] += 1
			a[1][i+j] += 1
			a[3][i - j + n - 1] += 1


f = open('305.txt','r')
k = int(f.readline().strip())
for l in range(k):
        a = []
        a.append(list(map(int, f.readline().split())))
        a.append(list(map(int, f.readline().split())))
        a.append(list(map(int, f.readline().split())))       #Работа с файлом
        a.append(list(map(int, f.readline().split())))
        c = [ i for i in a]
        n = len(a[2])
        m = len(a[0])
        result = [[0 for i in range(n)] for j in range (m)]
        count  =  sum (a[0])
        count0 = n * m - count
        find = False
        b = [[0 for i in range(m)],
                 [0 for i in range(m + n - 1)],
                 [0 for i in range(n)],
                 [0 for i in range(m + n - 1)],
              ]
        select(0, 0)
f.close()





























