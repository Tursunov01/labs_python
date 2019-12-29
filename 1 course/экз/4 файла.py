def make(n):
    #abc
    a = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','','thirteen',
        '','fifteen','','seventeen','nineteen']
    b = ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety','hundred',]
    if n <20:
        return a[n]
    s = ''
    x = n //100
    y = n // 10 %10
    z = n %10
    s = s+' ' +a[z]
    if y ==1:
        s = a[n%100]
    elif y>=1:
        s = b[y]+' '+s
    if x == 1:
        st = ' hundred '
    elif x == 0:
        st = ' '
    else:
        st = ' hundreds '
    s = a[x]+st+ s
    return s
def make_name(n):
    s = make(n%1000)
    if n// 1000 == 0:
        return s
    elif n // 1000 ==1:
        return 'one thousand '+s
    else:
        return make(n//1000)+ ' thousands '+s



def f3txt():
    result = ''
    f1 = open('f1.txt','r')
    f2 = open('f2.txt','r')
    s1 = f1.read().strip() + ' '
    s2 = f2.read().strip() + ' '
    c1 = 0
    c2 = 0
    while s1 != '' or s2 != '':
        if s1 == '':
                result += s2
                s2 = ''
        elif s2 == '':
                result += s1
                s1 = ''
        else:
            while c1<len(s1) and (s1[c1] != ' '):
                c1+=1
            while c2<len(s2) and (s2[c2] != ' '):
                c2+=1

            if int(s1[:c1]) > int(s2[:c2]):
                result += s2[:c2+1]
                s2 = s2[c2+1:]
                c2 = 0
            else:
                result +=s1[:c1+1]
                s1 = s1[c1+1:]
                c1 +=0

    f1.close()
    f2.close()
    return result

def f4txt():
    result = ''
    f3 = open('f3.txt','r')
    s = f3.read().strip() + ' '
    c = 0
    while s[c] != ' ':
        c +=1
    before = s[:c+1]
    s = s[c+1:]
    c = 0
    while s != '':
        while s[c] != ' ':
            c +=1
        if s[:c+1] != before:
            if int(before) %2 == 1:
                result += before
            else:
                result += before
            before = s[:c+1]
        s = s[c+1:]
    if int(before) %2 == 1:
        result += before
    else:
        result += before
    f3.close()
    return result
def gtxt():
    f = open('f4.txt','r')
    s = f.read().strip()+' '
    c = 0
    result = ''
    while s != '':
        while s[c] != ' ':
            c +=1
        result += s[:c+1]
        if int(s[:c+1]) %2 == 1: 
            result += ' {}\n'.format(make_name(int(s[:c+1])))
        else:
            result += '\n'
        s = s[c+1:]
        c = 0
    f.close()
    return result

def output(fname,st):
    f = open(fname,'w')
    f.write(st)
    f.close()
#main
output('f3.txt',f3txt())
output('f4.txt',f4txt())
output('g.txt',gtxt())
print('finished')
f = open('g.txt','r')
for line in f:
    print(line, end = '')
f.close()
