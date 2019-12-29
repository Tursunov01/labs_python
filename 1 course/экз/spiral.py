n = int(input())
m = n*(n+1)/2
x = m+1
j = 0
a = [[0]*n for i in range(n)]
while True:
    for i in range(j, n - j*2):
        x -= 1
        a[j][i] = x 

    if x == 1 : break

    for i in range(j+1, n-2*j-1):
        x -= 1
        a[i][n-i-1-j] = x
        
    if x == 1: break

    for i in range(n-1-j*2, j, -1):
        x -= 1
        a[i][j] = x

    if x == 1 : break
    
    j += 1

##for i in range(n):
##    for j in range(n):
##        print('{:3g}'.format(a[i][j]), end = '')
##print()
for q in a:
    print(q)
