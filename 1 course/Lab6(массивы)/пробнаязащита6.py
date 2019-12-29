
N = int(input('Input the number of elements: '))
b = []
for i in range(N):
    a =  int(input('Input element ' + str(i+1) + ' : '))
    b.append(a)
print(b)
posmn = 0
for i in range(0, len(b)):
    if float(b[i]) < float(b[posmn]):
        posmn = i

for k in range(posmn,len(b)):
    if float(b[posmn]) == float(b[k]):
        posmn = k
posmx = 0
for j in range(0,len(b)):
    if float(b[j]) > float(b[posmx]):
        posmx = j
c=0
for i in range(N):
    if posmn < i < posmx:
        c += 1
    elif c > 0:
         b[i-c] = b[i]
               
print(b[:N-c])    
