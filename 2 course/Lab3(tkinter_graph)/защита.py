def f(x):
    return x*x-4

def kasat(f,a, b, eps, k):
    z = []
    y1 = f(a)
    y2 = f(b)
    x0 = (a + b)/2
    xn = f(x0)
    n = 1
    if y1 *y2 > 0:
        code = 2
        x = "-"
        n = "-"
        start = "a-"
        konec = "b-"
        return code, x, n, start, konec
    if y1 * y2 < 0:
        xn1 = xn - (f(xn)/F(xn))
        y3 = f(xn1)
    while abs(y3) > eps:
        if y1 * y3 < 0:
            b = xn1
        else:
            a = xn1
        n += 1
    if k >= n:
        code = 0
        return(code, x, n,n_1,k_1)
    else:
        code = 1
        return (code, x, n, n_1,k_1)
        
    
def prk(a,b,n,eps, number):
    znachenie = []
    codes = []
    korni = []
    iterat = []
    nachalo = []
    konec = []
    step = int((b - a) / n)
    #print(step)
    for i in range(step):
        start = a + n *(i)
        #print(start)
        end = a + n *(i + 1)
        #print(end)
        code, x, k, a_1, a_2 = kasat(f,start,end,eps,number)
        if code == 1 or code == 0:
            codes.append(code)
        if x != "-":
            korni.append(x)
            znachenie.append(f(x))
        if k != "-":
            iterat.append(k)
        if a_1 != "a-":
            nachalo.append(a_1)
        if a_2 != "b-":
            konec.append(a_2)
    '''endd = b % n
    print(endd)
    ends = b - endd
    print(ends)'''
    code, x, k, a_1, a_2 = kasat(f,end,b,eps,number)
    if code == 1 or code == 0:
        codes.append(code)
    if x != "-":
        korni.append(x)
        znachenie.append(f(x))
    if k != "-":
        iterat.append(k)
    if a_1 != "a-":
        nachalo.append(a_1)
    if a_2 != "b-":
        konec.append(a_2)
    
    for i in range(len(korni) -2):
        if korni[i] == korni[i+1]:
            j = i
            korni.remove(korni[i])
        else:
            j = "-"
        for i in range(len(codes)):
            if i == j:
                codes.remove(codes[i])
        for i in range(len(znachenie)):
            if i == j:
                znachenie.remove(znachenie[i])
        for i in range(len(iterat)):
            if i == j:
                iterat.remove(iterat[i])
        for i in range(len(nachalo)):
            if i == j:
                nachalo.remove(nachalo[i])
        for i in range(len(konec)):
            if i == j:
                konec.remove(konec[i])
    return nachalo, konec, korni, znachenie, iterat, codes

nachalo, konec, korni, znachenie, iterat, codes = prk(-10,10,25,1e-5,25)
print(nachalo)
print(konec)
print(korni)
print(znachenie)
print(iterat)
print(codes)
