from math import sqrt

A = float(input("Введите координаты x1: "))
B = float(input("Введите координаты y1: "))
C = float(input("Введите координаты x2: "))
D = float(input("Введите координаты y2: "))
E = float(input("Введите координаты x3: "))
F = float(input("Введите координаты y3: "))
R = 1e-6#0.000001

a = sqrt(((C - A)**2)+((D - B)**2))
print("Сторона a =", a)
b = sqrt(((E - C)**2)+((F - D)**2))
print("Сторона b =", b)
c = sqrt(((E - A)**2)+((F - B)**2))
print("Сторона c =", c)

if a + b > c and b + c > a and a + c > b:
  if abs(a-b) < R or abs(b-c) < R or abs(a-c) < R:
     print("Треугольник является равнобедренным")
     if abs(a-b) < R:
         m = sqrt(4*(a**2)-c**2)/2
         print("m=: ",m)
     elif abs(b-c) < R:
         m = sqrt(4*(c**2)-a**2)/2
         print("m=: ",m)
     elif abs(a-c) < R:
         m = sqrt(4*(c**2)-b**2)/2
         print("m=: ",m)
  elif a == b and b == c and c ==a:
      m = a * sqrt(3) /(2)
  else:
      if a > c and a > b:
         m = sqrt(2*(c**2+b**2)-a**2)/2
         print("m=: ",m)
      elif c > a and c > b:
         m = sqrt(2*(a**2+b**2)-c**2)/2
         print("m=: ",m)
      elif b > a and b > c:
         m = sqrt(2*(a**2+c**2)-b**2)/2
         print("m=: ",m)
  
      
else:
    print("Такого треугольника не существует")
