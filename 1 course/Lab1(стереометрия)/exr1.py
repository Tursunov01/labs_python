from math import sqrt
A=int(input("Input A: "))
B=int(input("Input B: "))

if A>1:
    D=B**2-4*A

else: D=B**2+4*A

y1=(-B+sqrt(D))/2
y2=(-B-sqrt(D))/2

x1=y1+B
x2=y2+B

print("First pair of x;y is", x1,y1)
print("Second pair of x;y is", x2,y2)




    
