dlina = int(input("Vvedite dlinu massiva A: "))

A = [0]* dlina
for k in range(dlina):
    A[k] = int(input("Vvedite znachenie elementa "+str(k) + ": "))

B = [1] * dlina
D = []

for k in range(1,dlina):
    for m in range(k):
        if A[k] % A[m] == 0 and B[m] >= B[k]:
            B[k] = B[m] + 1


max = B[0]
nomer = 0
for k in range(dlina):
    if B[k] > max:
        max = B[k]
        nomer = k


G = [1] * dlina

for k in range(1,dlina):
    for m in range(k):
        if A[k] % A[m] == 0 and G[m] >= G[k] :
            G[k] = G[m] + 1
            if k == nomer:
             D.append(A[m])

    if k == nomer:
        D.append(A[k])
        break

brojac = 0

for k in range(dlina):
    print(B[k])

print()

for k in range(len(D)):
    print(D[k])


