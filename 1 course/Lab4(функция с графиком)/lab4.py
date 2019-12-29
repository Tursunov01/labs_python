from math import sqrt ,cos ,pi

x1 = float(input("Введите начальное значение для X:= "))
x2 = float(input("Введите конечное значение для X:= "))   #Ввод данных
step = float(input("Введите шаг:= "))

if x1 > x2:
  print("Поменяйте значения х местами")
else:
 print ('_________________________________________________')
 print ('⏐  x  ⏐      y1     ⏐      y2      ⏐      y3     ⏐')
 print ('̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅')


max=-11000
min=11000
n = int(((x2 - x1)/step)) + 1
for x in range (0,n):
  x = x1+step*x
  y1 = x**3+6.1*(x**2)-35.4*x-25.7
  y2 = x**2-cos(pi*x)
  if (y2 > max):
     max = y2
  if (y2 < min):
     min = y2
  y3 = sqrt(y1**2+y2**2)
  if  x1 in range (-999,1000) or x2 in range (-999,1000):
      print('⏐',"{:5.2f}".format(x),'⏐',"%10.2f" % (y1),'⏐', "%10.2f" % (y2),'⏐',"%10.2f" % (y3),'⏐')
      print('̅' *48)
  else:
     print ("{:.2f}".format(x),"{:10.0e}".format(y1), "{:10.0e}".format(y2), "{:10.0e}".format(y3))
     print ('̅'*34)

print()
print('y min= ',float('{:.2f}'.format(min)),'̅'*85,'y max= ',float('{:.2f}'.format(max)))
print()

n = int(((x2 - x1)/step)) + 1
for x in range(0,n):
  x = x1 + step
  
  if x == 0.0:
    print('-' * 150)
  y2 = x**2-cos(pi*x)#График
  y2= round(y2, 4)
  print ('⏐','{:5.1f}'.format(x),' '*round(((y2-min)/(max-min))*80),'*')
