f = open('305.txt','r')
a = []
for i in f:
    a.append(i.strip().split())
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i][1] > a[j][1]:
            a[i], a[j] = a[j], a[i]
f.close()
f = open('310.txt','w')
for i in a:
    f.write('{} {}\n'.format(i[0],i[1]))
f.close()
