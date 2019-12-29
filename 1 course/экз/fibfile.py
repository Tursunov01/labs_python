import os
file = open('file1.txt','r')
file2 = open('file.txt', 'r')
file3 = open('output.txt', 'w')

flag = 0
a = b = 1

while True:
    if flag == 2:
        break
    for line in open("file1.txt").readlines():
        if int(line) == a+b:
            file3.write(line)
            a = b
            b = int(line)
            flag = 0
            break
    
    for line in open("file2.txt").readlines():
        if int(line) == a+b:
            file3.write(line)
            a = b
            b =int(line)
            flag = 0
            break
    flag += 1
    
file.close()
file2.close()
file3.close()
