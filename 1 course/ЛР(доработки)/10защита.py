fm = open('10.txt','r')
fx = open('101.txt','w')
fx = open('101.txt','a+')
a = []
for i in fm:
    i = i.strip()
    l,r = 0,0
    s = 0
    while r<len(i):
        while l<len(i) and not ( "0"<=i[l]<='9'):
            l +=1
        r = l
        while r<len(i) and   ('9'>=i[r]>='0'):
            r+=1
        if r > 1:
            s += int(i[l:r])
        l, r = l+1, l+1
    a.append([s,i])
for i in a:
    if i[0]%2==0:
        fx.write(i[1])
for i in a:
    if i[0]%2==1:
        fx.write(i[1])
        
fm.close()
fx.close()
