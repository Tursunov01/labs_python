while True:
    try:
        N = int(input('Введите размер массива: '))
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
       el_list = ['e', '+', '-', '.']
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

print(A)
B = [1] * N1
D = []
for k in range(1, N1):
    for m in range(k):
        if A[k] % A[m] == 0 and B[m] >= B[k]:
            B[k] = B[m] + 1

max = B[0]
nomer = 0
for k in range(N1):
    if B[k] > max:
        max = B[k]
        nomer = k

G = [1] * N1

for k in range(1, N1):
    for m in range(k):
        if A[k] % A[m] == 0 and G[m] >= G[k]:
            G[k] = G[m] + 1
            if k == nomer:
             D.append(A[m])
    if k == nomer:
        D.append(A[k])
        break

for k in range(len(D)):
    print(D[k])
