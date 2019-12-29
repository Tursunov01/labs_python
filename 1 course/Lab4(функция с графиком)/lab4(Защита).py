from math import sin
x1 = float(input("Введите начальное значение для X:= "))
x2 = float(input("Введите конечное значение для X:= "))   #Ввод данных
step = float(input("Введите шаг:= "))


a = []
x = x1
while x <= x2:
    y = sin(x)
    x += step
    a.append(y)
ymax = max(a)
ymin = min(a)
'''n = int(((x2 - x1)/step)) + 1
for x in range (0,n):
  x = x1+step*x
  y = sin(x)
  if (y > max):
     max = y
  if (y < min):
     min = y'''
  
    
print()
print('y min= ','{:.2f}'.format(ymin),'̅'*85,'y max= ','{:.2f}'.format(ymax))
print()


n = int(((x2 - x1)/step)) + 1
for x in range(n):
  x = x1 + step*x
  y = sin(x)     #График
  #y = round(y, 4)
  print ('⏐','{:5.1f}'.format(x),' '*round(((y-ymin)/(ymax-ymin))*80),'*')
