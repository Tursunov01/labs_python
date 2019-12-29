from math import sqrt

A = float(input("Введите координаты x1: "))
B = float(input("Введите координаты y1: "))
C = float(input("Введите координаты x2: "))
D = float(input("Введите координаты y2: "))
E = float(input("Введите координаты x3: "))
F = float(input("Введите координаты y3: "))

R = 0.0001

a = sqrt(((C - A)**2)+((D - B)**2))
print("Сторона a =", a)
b = sqrt(((E - C)**2)+((F - D)**2))
print("Сторона b =", b)
c = sqrt(((E - A)**2)+((F - B)**2))
print("Сторона c =", c)

p = (a + b + c)/2
S = sqrt(p*(p-a)*(p-b)*(p-c))

if  a + b > c and b + c  > a and a + c > b:
  if abs(a-b) < R or abs(b-c) < R or abs(a-c) < R:
     print("Треугольник является равнобедренным")
  elif  a==b==c:
     L = a * sqrt(3) /(2)
     print("Треугольник равносторонний")
     print("Биссектриса L=", L)
  else:
       if c > a and c > b:
          L = sqrt((a*b*(a + b + c)*(a + b - c))/(a + b))
          print("L=", L)
       elif b > a and b > c:
          L = sqrt((a*c*(a + b + c)*(a + c - b))/(a + c))
          print("L=", L)
       elif a > c and a > b:
          L = sqrt((c*b*(a + b + c)*(c + b - a))/(c + b))
          print("L=", L)
else:
    print("Треугольник не существует")


M = float(input("Введите значение произвольного X=: "))
N = float(input("Введите значение произвольного Y=: "))

m = sqrt((A - M)**2+(B - N)**2)
n = sqrt((C - M)**2+(D - N)**2)
t = sqrt((E - M)**2+(F - N)**2)

p1 = (m + n +a)/2
S1 = sqrt(p1*(p1 - a)*(p1 - m)*(p1 - n))

p2 = (b + n + t)/2
S2 = sqrt(p2*(p2 - b)*(p2 - t)*(p2 - n))

p3 = (m + t + c)/2
S3 = sqrt(p3*(p3 - t)*(p3 - m)*(p3 - c))

S4 = S1 + S2 + S3

if round(S4) == round(S):
  if S1 > S2 and S1 > S3:
    h1 = 2*S1/a
    print("Наиболее удаленная расстояние равно", h1)
  elif S2 > S1 and S2 > S3:
      h2 = 2*S2/b
      print("Наиболее удаленная расстояние равно", h2)
  elif S3 > S1 and S3 > S2:
      h3 = 2*S3/c
      print("Наиболее удаленная расстояние равно", h3)
else:
  print("Точка вне треугольника")

     
