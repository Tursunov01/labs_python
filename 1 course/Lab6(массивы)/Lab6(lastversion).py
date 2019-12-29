while True:
    try:
        N = (input('Введите размер массива: '))
    except ValueError:
        print(' введите размер заного')
        continue
    else:
        break

N1 = int(N)
A = []
for i in range(N1):
    a1 = (input('Введите элемент №' + str(i+1) + ' первого массива: '))
    
    while True:
       el_list = ['e', '+', '.']
       if a1 == '' or a1[0] in el_list or a1[len(a1)-1] in el_list:
          print('Введите повторно элемент № ',i+1,' первого массива')
          a1 = (input())
          k=0
       else: 
           k2 = 0
           if a1[0] == '-':
               k = 1
           else:
              k = 0
           k3 = 0
           for m in range(len(a1)-1):

              if ((a1[m] == 'e') and (a1[m+1] == '-')) or ((a1[m] == 'e') and (a1[m+1] == '+')):
                    k3 += 1
                    n = m
           if (k3 == 1):
                    k += 2
           for q in range(len(a1)):
                if ('0' <= (a1[q]) <= '9'):
                        k += 1
                if   (a1[q] == '.') or (a1[q] == '.' and q < n):
                        k2 += 1
                if a1[q] == '.' and q > n:
                        k = 0 
           if k2 == 1:
                   k += 1
           if (k != len(a1)):
                 print('Введите повторно элемент № ',i+1,' первого массива')
                 a1 = (input())
                                
           else:
                 A.append(float(a1))
                 break

pos = 0
a = []
print(b)
for i in range(1, len(b)):
    if float(b[i]) < float(b[pos]):
        pos = i
for k in range(pos+1, len(b)):
    if float(b[k]) < 0:
        a.append(float(b[k]))
print(len(a))

