from math import sqrt

a = int(input("Input a: "))
b = int(input("Input b: "))
c = int(input("Input c: "))


if a == 0:
  if b == 0:
    if c == 0:
      print("X любой")
    else:
      print("Нет решений")
  else:
    x = -c/b
    print("x=: ", x)
else:
  
  D = b*b-4*a*c

  if D>0:
    X1 = ((-b)+sqrt(D))/(2*a)
    X2 = ((-b)-sqrt(D))/(2*a)
    print("X1=: ", X1)
    print("X2=: ", X2)
  if D==0:
    X = (-b)/(2*a)
    print("X=:", X )
  else:
    print("Нет решений")













