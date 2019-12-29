N = int(input('Input the number of elements: '))
b = []
c = []
for i in range(N):
    a =  int(input('Input element ' + str(i+1) + ' : '))
    b.append(a)
print(b)


for k in range(len(b)):
    summ = 0
    count = 0
    if b[k] > 0 :
        c.append(b[k])
        for j in range(0,k+1
                       ):
            summ += b[j]
            count +=1
        c.append(summ/count)
    elif k == 0 and b[k]>0:
        c.append(b[k])
        
    else:
        c.append(b[k])
print(c)
