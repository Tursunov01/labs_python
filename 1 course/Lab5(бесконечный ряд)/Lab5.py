#Турсунов Жасурбек

x = float(input('Input the value of x: '))
n = int(input('Input quantity of iterations: '))
e = float(input('Input accuracy of e: '))
r = int(input('Input step of print: '))

if n == 0 :
    print()
    print('Ряд не сойдется за 0 итераций')
elif r <= 0:
    print()
    print('Inpur the step bigger than 0')
elif n < 0:
     print()
     print('Ряд не сойдется из за отриц. итераций')
else:
    print('______________________________________________________')
    print('⏐   № of n  ⏐   Current member   ⏐    Current value   ⏐')
    print('̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅̅') 
    t = (x ** 3) / 3
    s = t
    k = 1
    while n >= k :         
          if k % r == 0 :
              print('⏐', "{:10g}".format(k), '⏐', "{:18.2g}".format(t), '⏐', "{:17.2g}".format(s), '⏐')
              print('̅' * 54)
          k += 1  
          t = (t * (-x * x) * (4 * (k - 1) * (k - 1) - 1)) / (4 * k * k - 1)
          s += t
          if abs(t) <= e:
             print('Ряд сошелся за ',k-1,'итераций')
             print('Общая сумма равна ',s)
             break         
    if (k-1 == n):
        print('Ряд не сошелся за ', n, ' итераций.')



