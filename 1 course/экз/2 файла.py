import os
def solution():
    fn = open('input1.txt','r')
    fm = open('input2.txt','r')
    fx = open('output.txt','w')
    fx = open('output.txt','w+')
    a = [i for i in fn]
    for line in fm:
        num1, num2, st = line.split()
        num1, num2 = int(num1), int(num2)
        s = a[num1 - 1]
        s = s[:num2] + st + s[num2:]
        fx.write(s.strip()+'\n')
    fx.seek(0)
    check = True
    for line in sorted(fx, key = len):
        if check:
            fx.seek(0)
            check = False
        fx.write(line)
    fx.close()
    fn.close()
    fm.close()
    
solution()
f = open('output.txt','r')
for line in f:
    print(line,end = '')
f.close()
os.remove('output.txt')
